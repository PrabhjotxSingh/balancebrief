from qdrant_client import QdrantClient

client = QdrantClient(
    url="https://e89b7298-c96f-4dbf-84ef-f0db87ed8f95.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="O6zlMt_wp8A3UoefaS-lEoCWZE1Zm6WplaOwKxjMhB3KSSMyTe405w",
)

from qdrant_client.http.models import Distance, VectorParams


from qdrant_client.http.models import PointStruct

data=[
        PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}),
        PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": "London"}),
        PointStruct(id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": "Moscow"}),
        PointStruct(id=4, vector=[0.18, 0.01, 0.85, 0.80], payload={"city": "New York"}),
        PointStruct(id=5, vector=[0.24, 0.18, 0.22, 0.44], payload={"city": "Beijing"}),
        PointStruct(id=6, vector=[0.35, 0.08, 0.11, 0.44], payload={"city": "Mumbai"}),
        PointStruct(id=7, vector=[0.35, 0.08, 0.11, 0.44], payload={"city": "Mama"}),
    ]

operation_info = client.upsert(
    collection_name="Sources",
    wait=True,
    points= data,
)
print(type(data)),

print(operation_info)