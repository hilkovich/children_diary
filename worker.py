import os
import pika
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("RABBIT_USER")
password = os.getenv("RABBIT_PASSWORD")
host = os.getenv("RABBIT_HOST")
port = os.getenv("RABBIT_PORT")

connection_params = pika.ConnectionParameters(
    host=host,
    port=port,
    virtual_host="/",
    credentials=pika.PlainCredentials(username=username, password=password),
)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()
