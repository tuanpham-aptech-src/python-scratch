from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from config.database import get_db
from app.models.product import Product, CreateProductDTO,RestockProductDTO, ListProductDTO

router = APIRouter(prefix="/products", tags=['products'])

@router.get("")
def get_all(search = "",db:Session = Depends(get_db)):
    query = db.query(Product)
    if search:
        # sử dụng or_: or_(s1, s2, ....)
        query = query.filter(or_(
            Product.name.ilike(f"%{search}%")
        )) # gán lại giá trị sau khi update
    # like, ilike
    products = query.all()

    # dùng dto để chuẩn hóa đầu ra.
    products_response = []
    for product in products:
        products_response.append(ListProductDTO.model_validate(product))
    return {
            "message": "Danh sách sản phẩm",
            "products": products_response
            }

@router.get("/{product_id}")
def create(product_id,db:Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first() # filter_by
    
    return {
            "message": "Chi tiết sản phẩm",
            "product": product
            }

@router.post("/{product_id}/restock")
def restock(payload: RestockProductDTO, product_id,db:Session = Depends(get_db)):
    if payload.stock_qty <= 0:
        raise HTTPException(status_code=400, detail={"message": "Số lượng sản phẩm phải lớn hơn 0"})
    
    product = db.query(Product).filter(Product.id == product_id).first() # filter_by
    if product == None:
        raise HTTPException(status_code=404, detail={"message": "Không tìm thấy sản phẩm"})
    
    product.stock_qty += payload.stock_qty
    # product.save()
    db.commit()
    db.refresh(product)
    
    return {
            "message": "Restock sản phẩm",
            "product": product
            }

@router.post("/")
def get_all(payload: CreateProductDTO,db:Session = Depends(get_db)):
    # validate ...
    if payload.price <= 0:
        raise HTTPException(status_code=400, detail={"message": "Giá sản phẩm phải lớn hơn 0"})
    
    if payload.stock_qty <= 0:
        raise HTTPException(status_code=400, detail={"message": "Số lượng sản phẩm phải lớn hơn 0"})
    
    product = Product(name=payload.name, price=payload.price, stock_qty=payload.stock_qty)
    db.add(product)
    db.commit()
    db.refresh(product)
    return {
            "message": "Tạo mới sản phẩm thành công",
            "product": product
            }


# Order (ok) -> order_items(fail: product_id bị sai, quantity: nhiều hơn stock)
# => kiểm tra transaction - roll back - commit .