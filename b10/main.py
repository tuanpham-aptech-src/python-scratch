from fastapi import FastAPI
import config.init_db
from app.routers.user import router as user_router
from app.routers.product import router as product_router
from app.routers.order import router as order_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)

@app.get('/hello')
def home():
    return {"message": "Ok 1234"}







