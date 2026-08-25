class Notification:
    def send(self):
        print("Sending notification")

class Email(Notification):
    def send(self):
        print("Sending Email")

class SMS(Notification):
    def send(self):
        print("Sending SMS")

class WhatsApp(Notification):
    def send(self):
        print("Sending WhatsApp message")

for notification in [Email(), SMS(), WhatsApp()]:
    notification.send()