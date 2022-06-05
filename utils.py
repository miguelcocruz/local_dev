import os

import psycopg2


def connect():
    username = os.getenv('WAREHOUSE_USER')
    password = os.getenv('WAREHOUSE_PASSWORD')
    host = os.getenv('WAREHOUSE_HOST')
    port = os.getenv('WAREHOUSE_PORT')
    connection_string = f"postgresql://{username}:{password}@{host}:{port}"
    return psycopg2.connect(connection_string)
