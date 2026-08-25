class Car:
    def start(self):
        print("Car starts")

class Bike:
    def start(self):
        print("Bike starts")

class Bus:
    def start(self):
        print("Bus starts")

for vehicle in [Car(), Bike(), Bus()]:
    vehicle.start()