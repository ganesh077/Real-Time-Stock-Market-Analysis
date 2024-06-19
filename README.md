# Stock Market Data Pipeline with Kafka and AWS

This project demonstrates a data pipeline that simulates stock market data, streams it through Apache Kafka, and stores the data in Amazon S3 for further processing and analysis with AWS Glue and Amazon Athena.

## Architecture

![Architecture Diagram]([Project Architecture.jpeg](https://github.com/ganesh077/Real-Time-Stock-Market-Analysis/blob/main/Project%20Architecture.jpeg))

## Components

1. **Stock Market Simulation**: A Python script (`kafkaproducer.py`) simulates stock market data.
2. **Kafka Producer**: Sends the simulated data to a Kafka topic.
3. **Kafka Consumer**: Reads data from the Kafka topic and writes it to Amazon S3.
4. **Data Storage**: Data is stored in Amazon S3 in JSON format.
5. **Data Processing and Analysis**: AWS Glue crawlers catalog the data, and Amazon Athena queries it.

## Setup and Installation

### Prerequisites

- AWS account with S3, EC2, and Glue services enabled.
- Python 3.x installed.
- Apache Kafka installed on an EC2 instance.
- Kafka-Python library installed.

### Step-by-Step Instructions

#### 1. Kafka Setup on EC2

```sh
# Download and extract Kafka
wget https://downloads.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz
tar -xvf kafka_2.12-3.3.1.tgz

# Install Java
sudo yum install java-1.8.0-openjdk

# Start ZooKeeper
cd kafka_2.12-3.3.1
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka server
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
bin/kafka-server-start.sh config/server.properties

# Create a Kafka topic
bin/kafka-topics.sh --create --topic demo_testing2 --bootstrap-server <EC2 Public IP>:9092 --replication-factor 1 --partitions 1
```

#### 2. Run Kafka producer
```
python kafkaproducer.py <path_to_csv_file>
```

#### 3. Run Kafka consumer
```
python kafkaconsumer.py <s3_bucket_path>
```



