from fastapi import FastAPI

app=FastAPI()

@app.get("/")

def hh():
    return {"message": "hi boss"}
