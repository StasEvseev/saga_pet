from flask import Flask
from kafka import KafkaConsumer
from flask import stream_with_context, Response
import msgpack

app = Flask(__name__)

consumer = KafkaConsumer(
    'saga_events',
    bootstrap_servers=['kafka'],
    value_deserializer=msgpack.unpackb
)


@app.route('/')
def hello_world():
    def generate():
        for message in consumer:
            yield "%s:%d:%d: key=%s value=%s<br/>" % (message.topic, message.partition, message.offset, message.key, message.value)

    return Response(stream_with_context(generate()))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
