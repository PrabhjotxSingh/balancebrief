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
    print(queryToSearch)
    result = runQuery(queryToSearch)
    print(result)
    return {"queryToSearch": queryToSearch}

@app.get("/grab")
def grab_variable():
    title = "title of article"
    summary = "summary of article"
    author = "author of article"
    return {"title": title, "summary": summary, "author": author}