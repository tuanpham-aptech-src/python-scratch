from abc import ABC, abstractmethod

class BaseAPIRequest(ABC):
    
    @abstractmethod
    def validate(self):
        pass