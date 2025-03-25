from flask import Blueprint, jsonify, current_app, request
from app.services.common_service import ping

common = Blueprint('api', __name__)

@common.route('/health', methods=['GET'])
def health_route():
    service_name = current_app.config["SERVICE_NAME"]
    return jsonify({'status': f'{service_name} running'}), 200

@common.route('/ping', methods=['GET'])
def ping_route():
    host = request.args.get('host')
    port = request.args.get('port', default=5000, type=int)
    data = ping(host=host, port=port)
    if "error" in data:
        return jsonify({"error": data["host not reachable"]}), 400
    return jsonify({"response": data})
