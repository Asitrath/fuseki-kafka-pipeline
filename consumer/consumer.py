from kafka import KafkaConsumer
import requests

def sanitize_triple(triple: str) -> str:
    triple = triple.strip()
    if not triple.endswith('.'):
        triple += ' .'
    return triple

consumer = KafkaConsumer('processed-triples', bootstrap_servers='kafka:9092')
fuseki_url = 'http://fuseki:3030/ds/update'

graph_uri = "http://example.org/g"

for msg in consumer:
    triple = sanitize_triple(msg.value.decode('utf-8'))
    sparql = f"INSERT DATA {{ GRAPH <{graph_uri}> {{ {triple} }} }}"
    res = requests.post(fuseki_url, data={'update': sparql}, auth=('admin', 'admin'))

    print("SPARQL:", sparql)
    print("Status:", res.status_code)
    print("Response:", res.text)
