from Payment.base_payment import Payment

class CreditCardPayment(Payment):
    def __init__(self, card_number:str):
        super().__init__()
        self.card_number = card_number
    
    def process_payment(self)->bool:
        return True
    
    def get_info(self)->str:
        return f"Credit Card: **** **** **** {self.card_number[-4:]}"