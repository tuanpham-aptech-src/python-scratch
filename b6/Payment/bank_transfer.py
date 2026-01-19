from Payment.base_payment import Payment

class BankPayment(Payment):
    def __init__(self, account_number:str):
        super().__init__()
        self.account_number = account_number
    
    def process_payment(self)->bool:
        return True
    
    def get_info(self)->str:
        return f"Bank Transfer. STK: {self.account_number}"