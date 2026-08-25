class Computer:
    def process(self):
        print("Computer processes data")

class Laptop(Computer):
    def process(self):
        print("Laptop processes data")

class Desktop(Computer):
    def process(self):
        print("Desktop processes data")

class Server(Computer):
    def process(self):
        print("Server processes data")

for computer in [Laptop(), Desktop(), Server()]:
    computer.process()