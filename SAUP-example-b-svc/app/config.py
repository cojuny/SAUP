import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVICE_NAME = os.getenv('SERVICE_NAME', 'unknown-service')
    SERVICE_PORT = os.getenv('SERVICE_PORT', 'unknown-port')
    KAFKA_SERVER = os.getenv('KAFKA_SERVER', 'kafka:9092')


