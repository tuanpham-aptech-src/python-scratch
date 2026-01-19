
from Payment.base_payment import Payment
from Payment.credit_card import CreditCardPayment
from Payment.momo import MomoPayment
from Payment.bank_transfer import BankPayment

def thanh_toan_don_hang(payment_method: Payment, so_tien):
    isSuccess = payment_method.process_payment()
    if(isSuccess):
        print(f"Đã thanh toán thành công số tiền {so_tien}")
        print(f"Phương thức thanh toán là {payment_method.get_info()}")
    else:
        print(f"Thanh toán thất bại {so_tien}")
        print(f"Phương thức thanh toán là {payment_method.get_info()}")

while True:
    print("1: Thẻ tín dụng (Credit Card)")
    print("2: Ví điện tử (Momo)")
    print("3: Chuyển khoản (Bank Transfer)")
    user_pick = input("Chọn phương thức thanh toán:")
    if user_pick == '1':
        payment_method = CreditCardPayment('23184115578787')
    elif user_pick == '2':
        payment_method = MomoPayment('0987987999')
    elif user_pick == '3':
        payment_method = BankPayment('04156789333')
    else:
        print("Chọn sai, vui lòng chọn lại")
        continue
    thanh_toan_don_hang(payment_method, 5_000_000)
    payment_method.moo()
    break
    

# Đã thanh toán thành công số tiền xxxx VNĐ
# Phương thức thanh toán là ....