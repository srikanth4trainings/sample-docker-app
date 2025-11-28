from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def loadUsers():
    return {"message":"Welcome to FastAPI"}