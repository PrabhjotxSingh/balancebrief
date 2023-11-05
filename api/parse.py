import os
import cohere
import numpy as np

from qdrant_client import QdrantClient
from cohere.responses.classify import Example
from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.http.models import PointStruct

client_Qdrant = QdrantClient(
    url="https://e89b7298-c96f-4dbf-84ef-f0db87ed8f95.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="O6zlMt_wp8A3UoefaS-lEoCWZE1Zm6WplaOwKxjMhB3KSSMyTe405w",
)


client_Cohere = cohere.Client('lqJD3VjaVUpo4tgxxzg2RFIuu6p3jXmmezQc0tXD')

os.chdir("api/sources/") 
  
def read_text_file(file_path): 
    text_file = open(file_path, "r")
    return text_file
meta_data = []
text = []
# iterate through all file 
for file in os.listdir(): 
    # Check whether file is in text format or not 
    if file.endswith(".txt"): 
        file_path = f"{file}"

        # call read text file function
        text_file = read_text_file(file_path)
        temp = []
        for x in range(4):
            temp += [text_file.readline().replace("\n", '')]
        text_file.readline()
        body = [text_file.read().rstrip().replace("\n", ' ')]
        text +=  body
        temp += body
        meta_data.append(temp)
#Encode your documents with input type 'search_document'
doc_emb = client_Cohere.embed(text, input_type="search_document", model="embed-english-v3.0").embeddings

#Consolidate all captured data into a list of PointStructs to send to qDrant collection
data = [PointStruct(id=i + 1, vector=doc_emb[i], payload = {"Bias": meta_data[i][0], "Author": meta_data[i][1], "Title": meta_data[i][2], "URL": meta_data[i][3], "Text": meta_data[i][4]}) for i in range(0, len(meta_data))]
operation_info = client_Qdrant.upsert(
    collection_name="Sources",
    wait=True,
    points= data,
)
print(data)