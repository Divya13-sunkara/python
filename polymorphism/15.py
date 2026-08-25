class Payment:
    def pay(self):
        print("Payment")

class UPI(Payment):
    def pay(self):
        print("Payment through UPI")

class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card")

class NetBanking(Payment):
    def pay(self):
        print("Payment through Net Banking")

for payment in [UPI(), CreditCard(), NetBanking()]:
    payment.pay()