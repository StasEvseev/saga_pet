from django.db import models


class Order(models.Model):
    customer_id = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=5)


class Outbox(models.Model):
    topic = models.CharField(max_length=200)
    body = models.TextField()
    sent = models.BooleanField(default=False)


class Transaction(models.Model):
    event = models.CharField(max_length=200)
