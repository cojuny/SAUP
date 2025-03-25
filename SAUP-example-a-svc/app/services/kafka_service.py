from kafka import KafkaProducer, KafkaConsumer
from flask import current_app
from multiprocessing import Process, Event

producer = None
consumer_process = None
stop_event = Event()

# Initialize Kafka producer (lazy initialization)
def get_producer():
    global producer
    if producer is None:
        kafka_server = str(current_app.config['KAFKA_SERVER'])
        producer = KafkaProducer(bootstrap_servers=kafka_server)
    return producer

def produce(message, topic='default-topic'):
    p = get_producer()
    p.send(topic, message.encode('utf-8'))
    p.flush()

def _consume_loop(topic, stop_event, kafka_server):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=kafka_server,
        auto_offset_reset='earliest',
        value_deserializer=lambda v: v.decode('utf-8')
    )
    print(f"[{topic}] Consumer started")

    while not stop_event.is_set():
        for msg in consumer:
            print(f"[{topic}] Consumed: {msg.value}")
            if stop_event.is_set():
                break

    consumer.close()
    print(f"[{topic}] Consumer stopped")

def start_consume(topic='default-topic'):
    global consumer_process, stop_event
    kafka_server = str(current_app.config['KAFKA_SERVER'])
    stop_event = Event()  # Create new Event per start
    consumer_process = Process(target=_consume_loop, args=(topic, stop_event, kafka_server))
    consumer_process.start()
    print(f"{topic} start consume.")

def end_consume():
    global consumer_process, stop_event
    if stop_event:
        stop_event.set()
    if consumer_process:
        consumer_process.join()
        consumer_process = None
        stop_event = None
    print(f"end consume.")