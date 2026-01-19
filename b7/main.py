from fastapi import FastAPI
from pydantic import BaseModel
from app.database.mock_db import mock_data
from app.core.request.product.CreateProductRequest import CreateProductRequest
from app.core.api.BaseAPIResponse import BaseAPIResponse
from app.core.api.Response import SuccessResponse

app = FastAPI()
class Item(BaseModel):
    name: str

@app.get('/')
def home():
    return {"message": 'Welcome to FastAPI!'}

@app.get('/items/{item_id}')
def getDetailItem(item_id:int):
    return {"message": 'Get detail Item', "item_id": item_id}

@app.get('/items')
def getListItems(page:int = 1, per_page:int = 10):
    return {"message": 'Get list Items', "pagination": {
        "page": page,
        "per_page": per_page,
        "items": mock_data
    }}

@app.post('/items')
def createItem(item:CreateProductRequest)->BaseAPIResponse:
    # item.validate()
    return SuccessResponse('Tạo item thành công', item).to_json()



# CRUD
"""
cấu trúc response
{
    status_code: int,
    success: bool,
    data: any,
    message: str,
}
"""