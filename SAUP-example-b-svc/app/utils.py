import requests

def call_external_service(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise exception for HTTP 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to call {url}: {e}")
        return {"error": str(e)}
    
