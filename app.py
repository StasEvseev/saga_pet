from flask import Flask
from kafka import KafkaProducer
import msgpack
import json
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

producer = KafkaProducer(
    bootstrap_servers=['kafka'],
    value_serializer=msgpack.dumps
)


@app.route('/')
def hello_world():
    producer.send(topic='saga_events', value={'view': 'hello_world'})
    return 'Hello World!'


@app.route('/order/<customer_id>/<amount>')
def order_view(customer_id, amount):
    transaction_id = cache.incr('transaction_id')

    producer.send(
        topic='saga_events',
        value={
            'transaction_id': transaction_id,
            'customer_id': customer_id,
            'action': 'reserve_money',
            'amount': amount
        }
    )


@app.route('/payment/<customer_id>/<amount>/')
def payment(customer_id, amount):
    transaction_id = cache.incr('transaction_id')

    producer.send(
        topic='saga_events',
        value={
            'transaction_id': transaction_id,
            'customer_id': customer_id,
            'action': 'reserve_money',
            'amount': amount
        }
    )


@app.route('/database/<type>')
def database(type):
    return json.dumps(cache.get(f'DATABASE{type}'), indent=4)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
