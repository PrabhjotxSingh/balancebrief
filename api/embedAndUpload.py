import os
import cohere
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct

from dotenv import load_dotenv

load_dotenv()

COHERE_KEY = os.getenv('COHERE_API_CREDENTIAL')
QDRANT_KEY = os.getenv('QDRANT_API_CREDENTIAL')

client_Qdrant = QdrantClient(
    url="https://e89b7298-c96f-4dbf-84ef-f0db87ed8f95.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key=QDRANT_KEY,
)

client_Cohere = cohere.Client(QDRANT_KEY)

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

#Insert the embedded data and meta data to qDrant
operation_info = client_Qdrant.upsert(
    collection_name="Sources",
    wait=True,
    points= data,
)
