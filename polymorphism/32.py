class UPIPayment:
    def pay(self):
        print("Payment through UPI")

class CardPayment:
    def pay(self):
        print("Payment through Card")

class CashPayment:
    def pay(self):
        print("Payment through Cash")

def process_payment(payment):
    payment.pay()

process_payment(UPIPayment())
process_payment(CardPayment())
process_payment(CashPayment())