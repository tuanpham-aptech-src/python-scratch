from fastapi import  Header, HTTPException
SECRET_API_KEY = '1a2b'

def check_header_x_key(x_user_id:str = Header(...)):
    if x_user_id != SECRET_API_KEY:
        raise HTTPException(status_code=401, detail={"message": "x_user_id key truyền lên không đúng hoặc không truyền"})
    