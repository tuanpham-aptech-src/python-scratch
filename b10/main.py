from fastapi import FastAPI
import config.init_db
from app.routers.user import router

app = FastAPI()

app.include_router(router)

@app.get('/hello')
def home():
    return {"message": "Ok 1234"}







