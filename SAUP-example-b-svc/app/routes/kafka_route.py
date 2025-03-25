from flask import Blueprint, request, jsonify
from app.services.kafka_service import produce, start_consume, end_consume

kafka = Blueprint('kafka', __name__)

@kafka.route('/produce', methods=['POST'])
def produce_route():
    topic = request.json.get('topic')
    message = request.json.get('message')
    produce(message, topic=topic)
    return jsonify({'status': 'Message sent'})

@kafka.route('/consume_start', methods=['POST'])
def start_route():
    topic = request.json.get('topic')
    start_consume(topic=topic)
    return jsonify({'status': 'Consumer started'})

@kafka.route('/consume_stop', methods=['POST'])
def stop_route():
    end_consume()
    print('request received')
    return jsonify({'status': 'Consumer stopped'})