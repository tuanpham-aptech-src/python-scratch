from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=['users'])

@router.get("")
def get_all():
    return {"message": "ok - đây là danh sách users"}