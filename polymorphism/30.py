class DebitCard:
    def pay(self):
        print("Payment using Debit Card")

class CreditCard:
    def pay(self):
        print("Payment using Credit Card")

def process_card(card):
    card.pay()

process_card(DebitCard())
process_card(CreditCard())