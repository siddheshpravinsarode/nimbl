from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def getter():
    return {"msg": "Hello World"}

