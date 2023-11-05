import cohere
import os
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue
from dotenv import load_dotenv


def runQuery(queryIn):

    load_dotenv()
    #Setting up keys
    COHERE_KEY = os.getenv('COHERE_API_CREDENTIAL')
    QDRANT_KEY = os.getenv('QDRANT_API_CREDENTIAL')

    #Initializing clients
    client_Qdrant = QdrantClient(
        url="https://e89b7298-c96f-4dbf-84ef-f0db87ed8f95.us-east4-0.gcp.cloud.qdrant.io:6333", 
        api_key=QDRANT_KEY,
    )
    client_Cohere = cohere.Client(COHERE_KEY)

    #Setting default rejection json in case no suitable match found
    rejectJson = {"summary": "No records found to be a close enough match", "title": "Try Another Search", 
            "leftAuthor": "Author Not Available", "centerAuthor": "Author Not Available", "rightAuthor": "Author Not Available",
            "leftTitle": "Title Not Available", "centerTitle": "Title Not Available", "rightTitle": "Title Not Available",
            "leftSource": "Source Not Available", "centerSource": "Source Not Available", "rightSource": "Source Not Available"
            }

    query = queryIn

    #Encode query'
    query_emb = client_Cohere.embed([query], input_type="search_query", model="embed-english-v3.0").embeddings

    #Compute cos similarity with left biased weighted vectors in Qdrant
    search_result_left = client_Qdrant.search(
        collection_name="Sources",
        query_vector=query_emb[0],
        query_filter=Filter(
            must=[FieldCondition(key="Bias", match=MatchValue(value="Left"))]
        ),
        limit=1, #Return the top match
    )
     #Compute cos similarity with right biased weighted vectors in Qdrant
    search_result_right = client_Qdrant.search(
        collection_name="Sources",
        query_vector=query_emb[0],
        query_filter=Filter(
            must=[FieldCondition(key="Bias", match=MatchValue(value="Right"))]
        ),
        limit=1,
    )
     #Compute cos similarity with central biased weighted vectors in Qdrant
    search_result_central = client_Qdrant.search(
        collection_name="Sources",
        query_vector=query_emb[0],
        query_filter=Filter(
            must=[FieldCondition(key="Bias", match=MatchValue(value="Center"))]
        ),
        limit=1,
    )

    #Begin checking to see if matching records were found for each category
    if search_result_left and search_result_right and search_result_central:
        left = search_result_left[0].score
        center = search_result_central[0].score
        right = search_result_right[0].score

        #Checking if scores meet the threshold
        if ((left + center + right) / 3 > .3):
            #If all 3 are good, pass in full concated text body to summarize from all 3 biases
            balance = search_result_central[0].payload["Text"] + search_result_left[0].payload["Text"] + search_result_right[0].payload["Text"]
        else:
            #If average does not meet criteria, reject the search
            return rejectJson
        
    #If not all three had matching records, check if central was found and check similarity
    elif (search_result_central and search_result_central[0].score > .3):

        #If similarity is sufficient, use central only to generate full summary, as either left, right, or both bias's are missing
        search_result_left[0].payload["Author"] = "Author Not Available"
        search_result_left[0].payload["Title"] = "Title Not Available"
        search_result_left[0].payload["URL"] = "URL Not Available"
        search_result_right[0].payload["Author"] = "Author Not Available"
        search_result_right[0].payload["Title"] = "Title Not Available"
        search_result_right[0].payload["URL"] = "URL Not Available"
        balance = search_result_central[0].payload["Text"]

    #If left and right are present and have sufficient similarity, use them both minus the central bias to generate summary
    elif (search_result_left and search_result_right and ((search_result_left[0].score + search_result_left[0].score) / 2) > .3):
        search_result_central[0].payload["Author"] = "Author Not Available"
        search_result_central[0].payload["Title"] = "Title Not Available"
        search_result_central[0].payload["URL"] = "URL Not Available"
        balance = search_result_right[0].payload["Text"] + search_result_left[0].payload["Text"]
    else:
        return rejectJson #Last case, should reject anything else
    
    #Finally generate, the summarization using whatever articles are pulled and relevant
    response = client_Cohere.summarize(
        text=balance,
        format= 'paragraph',
        model='command',
        length='long'
        ,additional_command="Prioritize factual statements"
    )

    #Concatenating the titles to generate a new title
    titles = search_result_central[0].payload["Title"] + ". 2. " +  search_result_left[0].payload["Title"] + ". 3. " + search_result_right[0].payload["Title"]
    newTitle = client_Cohere.generate(prompt = ("Generate a title for a summarization of the following 3 articles: 1. " + titles))

    #Returning the final json Object with the full responsee
    return {"summary": response.summary, "title": newTitle[0].text, 
            "leftAuthor": search_result_left[0].payload["Author"], "centerAuthor": search_result_central[0].payload["Author"], "rightAuthor": search_result_right[0].payload["Author"],
            "leftTitle": search_result_left[0].payload["Title"], "centerTitle": search_result_central[0].payload["Title"], "rightTitle": search_result_right[0].payload["Title"],
            "leftSource": search_result_left[0].payload["URL"], "centerSource": search_result_central[0].payload["URL"], "rightSource": search_result_right[0].payload["URL"]
            }
