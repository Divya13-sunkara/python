class UPIPayment:
    def pay(self):
        print("Payment through UPI")

class CardPayment:
    def pay(self):
        print("Payment through Card")

class CashPayment:
    def pay(self):
        print("Payment through Cash")

for payment in [UPIPayment(), CardPayment(), CashPayment()]:
    payment.pay()