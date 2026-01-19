from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Any
from fastapi.responses import JSONResponse

class BaseAPIResponse(ABC, BaseModel):
    status_code: int
    message: str
    data: Any 
    
    def response(self):
        content =  {
            "status_code": self.status_code,
            "message": self.message,
            "data": self.data,
            }
        return JSONResponse(status_code=self.status_code, content=content)
    
