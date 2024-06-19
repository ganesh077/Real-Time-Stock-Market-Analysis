import pandas as pd
from kafka import KafkaProducer
from json import dumps
from time import sleep
import os
import sys

def create_kafka_producer():
    kafka_ip = 'EC2-IP'
    kafka_port = '9092'
    return KafkaProducer(bootstrap_servers=[f'{kafka_ip}:{kafka_port}'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

def main(file_path):
    try:
        producer = create_kafka_producer()
        df = pd.read_csv(file_path)
        print(df.head())  # Debug: Preview first few rows of data

        while True:
            try:
                dict_stock = df.sample(1).to_dict(orient="records")[0]
                producer.send('demo_testing2', value=dict_stock)
                sleep(1)
            except Exception as e:
                print(f"Failed to send message: {e}", file=sys.stderr)
                sleep(5)  # Wait before trying to send again

    finally:
        producer.flush()
        producer.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_csv_file>")
        sys.exit(1)
    main(sys.argv[1])
