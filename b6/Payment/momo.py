from Payment.base_payment import Payment

class MomoPayment(Payment):
    def __init__(self, phone_number:str):
        super().__init__()
        self.phone_number = phone_number
    
    def process_payment(self)->bool:
        return False
    
    def get_info(self)->str:
        return f"Ví Momo. Momo Phone Number:  {self.phone_number}"