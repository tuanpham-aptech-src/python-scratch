from abc import ABC, abstractmethod
import json
from pydantic import BaseModel
class BaseAPIResponse(ABC, BaseModel):

    def __init__(self, status_code:int , message:str, data = None):
        super().__init__()
        self.status_code = status_code
        self.message = message
        self.data = data

    def to_json(self):
        return json.dumps({
            "status_code": self.status_code,
            "message": self.message,
            "data": self.data,
            })