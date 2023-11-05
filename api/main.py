from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/query")
async def get_data(request: Request, queryToSearch: str):
    return {"queryToSearch": queryToSearch}