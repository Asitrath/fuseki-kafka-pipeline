import requests

def count_triples():
    query = "SELECT (COUNT(*) as ?count) WHERE { ?s ?p ?o }"
    res = requests.post(
        'http://localhost:3030/ds/query',
        data={'query': query},
        headers={'Accept': 'application/sparql-results+json'},
        auth=('admin', 'admin')
    )
    print("Triple count:", res.json()['results']['bindings'][0]['count']['value'])

