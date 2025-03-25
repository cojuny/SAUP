import app.utils as utils

def ping(host, port):
    url = f"http://{host}:{port}/health"
    response = utils.call_external_service(url)
    return response

