import cohere
import os
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue
from dotenv import load_dotenv

load_dotenv()

COHERE_KEY = os.getenv('COHERE_API_CREDENTIAL')
QDRANT_KEY = os.getenv('QDRANT_API_CREDENTIAL')
client_Qdrant = QdrantClient(
    url="https://e89b7298-c96f-4dbf-84ef-f0db87ed8f95.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key=QDRANT_KEY,
)
client_Cohere = cohere.Client(COHERE_KEY)

query = "China emissions rising?"

#Encode your documents with input type 'search_document'
query_emb = client_Cohere.embed([query], input_type="search_query", model="embed-english-v3.0").embeddings


search_result_left = client_Qdrant.search(
    collection_name="Sources",
    query_vector=query_emb[0],
    query_filter=Filter(
        must=[FieldCondition(key="Bias", match=MatchValue(value="Left"))]
    ),
    limit=1,
)
search_result_right = client_Qdrant.search(
    collection_name="Sources",
    query_vector=query_emb[0],
    query_filter=Filter(
        must=[FieldCondition(key="Bias", match=MatchValue(value="Right"))]
    ),
    limit=1,
)
search_result_central = client_Qdrant.search(
    collection_name="Sources",
    query_vector=query_emb[0],
    query_filter=Filter(
        must=[FieldCondition(key="Bias", match=MatchValue(value="Center"))]
    ),
    limit=1,
)

#print(search_result_central[0].payload["Text"])

balance = search_result_central[0].payload["Text"] + search_result_left[0].payload["Text"] + search_result_right[0].payload["Text"]
#print(balance)
response = client_Cohere.summarize(
    text=balance,
    format= 'paragraph',
    model='command',
    additional_command="Prioritize factual statements"
    )

print("New summary: " + response.summary)
