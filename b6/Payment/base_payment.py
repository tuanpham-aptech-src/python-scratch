from abc import ABC, abstractmethod
class Payment(ABC):
    # Phương thức thanh toán chung, True -> Thành công, False -> thất bại
    @abstractmethod
    def process_payment(self)-> bool:
        pass
    
    # lấy thông tin phương thức thanh toán
    @abstractmethod
    def get_info(self) -> str:
        pass

    def moo(self):
        print(f"Moooooooo!")