from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from config.database import get_db
from app.models.order import Order, CreateOrderDTO, ListOrderDTO, DetailOrderDTO
from app.models.user import User
from app.models.product import Product
from app.models.order_item import OrderItem
from app.utils.check_key import check_header_x_key
router = APIRouter(prefix="/orders", tags=['orders'], dependencies=[Depends(check_header_x_key)])

@router.get("")
def get_all(status = None, user_id: None | int = None,db:Session = Depends(get_db)):
    query = db.query(Order)
    if status:
        query = query.filter(Order.status == status)
    if user_id:
        query = query.filter(Order.user_id == user_id)

    results = query.all()
    orders = []
    for order in results:
        orders.append(ListOrderDTO.model_validate(order))

    return {
            "message": "Danh sách Order",
            "orders": orders
            }

@router.get("/{order_id}")
def get_all(order_id:int ,db:Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
            raise HTTPException(status_code=404, detail= {"message": "Không tìm thấy order"})
    data = DetailOrderDTO.model_validate(order)
    return {
            "message": "Chi tiết Order",
            "order": data
            }

@router.post("")
def create(body: CreateOrderDTO, db:Session = Depends(get_db)):
    # Validate: user_id tồn tại
    user = db.query(User).filter(User.id == body.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail= {"message": "người dùng không tồn tại"})

    # tạo nhanh 1 order nhưng KHÔNG commit
    order = Order(user_id= body.user_id)

    # Validate: các product_id trong items tồn tại và có đủ stock_qty
    # note: trong thực tế cần dùng select for update và transaction + commit
    for item in body.items: 
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=400, detail= {"message": "sản phẩm không tồn tại"})
        
        if item.quantity > product.stock_qty:
            raise HTTPException(status_code=400, detail= {"message": f"sản phẩm {product.name} có số lượng tồn kho không đủ"})
        # sử dụng tính chất back_populate của ORM
        order.items.append(OrderItem(order_id=order.id, 
                               product_id= product.id, 
                               quantity = item.quantity,
                               snapshot_price= product.price
                               ))
        product.stock_qty -= item.quantity

    db.add(order)
    db.commit()    

    return {
        "message": "Tạo order thành công",
        "payload": body
    }