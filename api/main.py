from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from compareQuery import runQuery

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Adjust to match the origin of your Angular app
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/query")
async def get_data(request: Request, queryToSearch: str):
    global result
    result = runQuery(queryToSearch)
    return {"queryToSearch": queryToSearch}

@app.get("/grab")
def grab_variable():
    title = result["title"]
    leftTitle = result["leftTitle"]
    rightTitle = result["rightTitle"]
    centerTitle = result["centerTitle"]
    summary = result["summary"]
    rightAuthor = result["rightAuthor"]
    leftAuthor = result["leftAuthor"]
    centerAuthor = result["centerAuthor"]
    rightSource = result["rightSource"]
    leftSource = result["leftSource"]
    centerSource = result["centerSource"]
    return {"title": title, "summary": summary, "leftTitle": leftTitle, "rightTitle": rightTitle, "centerTitle": centerTitle, "rightAuthor": rightAuthor, "leftAuthor": leftAuthor, "centerAuthor": centerAuthor, "rightSource": rightSource, "leftSource": leftSource, "centerSource": centerSource}