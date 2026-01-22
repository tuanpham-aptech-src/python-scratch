from fastapi import FastAPI
import config.init_db

app = FastAPI()

@app.get('/hello')
def home():
    return {"message": "Ok 1234"}







