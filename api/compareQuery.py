import cohere
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue

query = "Impeachment"

client_Qdrant = QdrantClient(
    url="https://e89b7298-c96f-4dbf-84ef-f0db87ed8f95.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="O6zlMt_wp8A3UoefaS-lEoCWZE1Zm6WplaOwKxjMhB3KSSMyTe405w",
)
client_Cohere = cohere.Client('lqJD3VjaVUpo4tgxxzg2RFIuu6p3jXmmezQc0tXD')

#Encode your documents with input type 'search_document'
query_emb = client_Cohere.embed([query], input_type="search_query", model="embed-english-v3.0").embeddings


search_result_left = client_Qdrant.search(
    collection_name="Sources",
    query_vector=query_emb[0],
    query_filter=Filter(
        must=[FieldCondition(key="Bias", match=MatchValue(value="Left"))]
    ),
    limit=3,
)
search_result_right = client_Qdrant.search(
    collection_name="Sources",
    query_vector=query_emb[0],
    query_filter=Filter(
        must=[FieldCondition(key="Bias", match=MatchValue(value="Right"))]
    ),
    limit=3,
)
search_result_central = client_Qdrant.search(
    collection_name="Sources",
    query_vector=query_emb[0],
    query_filter=Filter(
        must=[FieldCondition(key="Bias", match=MatchValue(value="Center"))]
    ),
    limit=3,
)
for result in search_result_central:
    print(result.payload["Bias"])
    print(result.score)
print(search_result_central)
#print(search_result_central[0].payload["Text"])