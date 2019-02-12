import json

from django.db.transaction import atomic
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from kafka import KafkaProducer
import msgpack
from .models import Order, Outbox, Transaction
import uuid


producer = KafkaProducer(
    bootstrap_servers=['kafka'],
    value_serializer=msgpack.dumps
)


@atomic
def place_order(customer_id, amount):
    Order.objects.create(customer_id=customer_id, amount=amount)

    if amount < 0:
        raise Exception("wrong value")

    transaction = Transaction.objects.create(event=str(uuid.uuid4()))

    Outbox.objects.create(
        topic="saga_events",
        body=json.dumps({
            "transaction_id": transaction.event,
            "customer_id": customer_id,
            "event": "place_order",
            "amount": amount
        })
    )


@atomic
def place_order_view(request, customer_id, amount):
    print(customer_id, amount)

    try:
        place_order(customer_id=customer_id, amount=amount)
    except Exception:
        return HttpResponseBadRequest()

    return HttpResponse(customer_id)
