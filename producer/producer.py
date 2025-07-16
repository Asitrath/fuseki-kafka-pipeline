from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import random
import time

# Retry logic for Kafka connection
while True:
    try:
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        print("Connected to Kafka!")
        break
    except NoBrokersAvailable:
        print("Kafka broker not available. Retrying in 5 seconds...")
        time.sleep(5)

# Send exactly 100 RDF triples
for _ in range(100):
    subject = f"<http://example.org/item/{random.randint(1, 100)}>"
    predicate = "<http://example.org/value>"
    value = random.randint(1, 100)
    obj = f"\"{value}\"^^<http://www.w3.org/2001/XMLSchema#integer>"
    triple = f"{subject} {predicate} {obj} ."
    
    producer.send('raw-triples', triple.encode('utf-8'))
    print("Sent:", triple)
    time.sleep(1)

print("Finished sending 100 triples.")
