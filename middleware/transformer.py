from kafka import KafkaConsumer, KafkaProducer
import re

consumer = KafkaConsumer('raw-triples', bootstrap_servers='kafka:9092')
producer = KafkaProducer(bootstrap_servers='kafka:9092')

pattern = r"\"(\d+)\""

for msg in consumer:
    triple = msg.value.decode('utf-8')
    updated = re.sub(pattern, lambda m: f"\"{int(m.group(1)) * 10}\"", triple)
    producer.send('processed-triples', updated.encode('utf-8'))
    print("Transformed:", updated)
