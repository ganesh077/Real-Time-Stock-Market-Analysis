from kafka import KafkaConsumer
import json
import os
from s3fs import S3FileSystem
import sys

def create_consumer():
    kafka_ip = 'EC2-IP'
    kafka_port = '9092'
    
    return KafkaConsumer(
        'demo_testing2',
        bootstrap_servers=[f'{kafka_ip}:{kafka_port}'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
        )

def main(bucket_path):
    consumer = create_consumer()
    s3 = S3FileSystem()

    try:
        for count, message in enumerate(consumer):
            file_path = f"{bucket_path}/stock_market_{count}.json"
            try:
                with s3.open(file_path, 'w') as file:
                    json.dump(message.value, file)
            except Exception as e:
                print(f"Failed to write to S3: {e}", file=sys.stderr)
            if count % 100 == 0:
                print(f"Processed {count} messages.")
    except KeyboardInterrupt:
        print("Stopped by user.")
    except Exception as e:
        print(f"Error processing messages: {e}", file=sys.stderr)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <s3_bucket_path>")
        sys.exit(1)
    main(sys.argv[1])
