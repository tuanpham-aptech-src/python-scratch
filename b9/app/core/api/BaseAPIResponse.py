from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Any
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class BaseAPIResponse(ABC, BaseModel):
    status_code: int
    message: str
    data: Any = None
    
    def response(self):
        content =  {
            "status_code": self.status_code,
            "message": self.message,
            "data": jsonable_encoder(self.data), # Chuyển hóa đối tượng thành JSON
        }

        return JSONResponse(status_code=self.status_code, content=content)
    
