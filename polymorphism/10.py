class Android:
    def show_features(self):
        print("Android supports customization")

class iPhone:
    def show_features(self):
        print("iPhone supports iOS features")

class WindowsPhone:
    def show_features(self):
        print("Windows Phone supports Windows features")

for phone in [Android(), iPhone(), WindowsPhone()]:
    phone.show_features()