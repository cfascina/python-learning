class Car():
    def __init__(self, wheels = 4):
        self.wheels = wheels

class Gasoline(Car):
    def __init__(self, engine = "Gasoline", tank_capacity = 50):
        Car.__init__(self)
        self.engine = engine
        self.tank_capacity = tank_capacity
        self.tank_status = self.tank_capacity * 0.3

    def refuel(self):
        self.tank_status = self.tank_capacity

class Eletric(Car):
    def __init__(self, engine = "Eletric", kwh_capacity = 60):
        Car.__init__(self)
        self.engine = engine
        self.kwh_capacity = kwh_capacity
        self.kwh_status = self.kwh_capacity * 0.3

    def recharge(self):
        self.kwh_status = self.kwh_capacity

class Hybrid(Gasoline, Eletric):
    def __init__(self, engine = "Hybrid", tank_capacity = 20, kwh_capacity = 10):
        Gasoline.__init__(self, engine, tank_capacity)
        Eletric.__init__(self, engine, kwh_capacity)

clio = Gasoline()
print("From Gasoline():")
print(f"Clio engine: {clio.engine}")
print(f"Clio tank capacity: {clio.tank_capacity}")
print(f"Clio tank status: {clio.tank_status}")
clio.refuel()
print("clio.refuel()")
print(f"Clio tank status: {clio.tank_status}")

zoe = Eletric()
print("\nFrom Eletric():")
print(f"Zoe engine: {zoe.engine}")
print(f"Zoe kWh capacity: {zoe.kwh_capacity}")
print(f"Zoe kWh status: {zoe.kwh_status}")
zoe.recharge()
print("zoe.recharge()")
print(f"Zoe kWh status: {zoe.kwh_status}")

prius = Hybrid()
print("\nFrom Hybrid():")
print(f"Prius engine: {prius.engine}")
print(f"Prius tank capacity: {prius.tank_capacity}")
print(f"Prius tank status: {prius.tank_status}")
print(f"Prius kWh capacity: {prius.kwh_capacity}")
print(f"Prius kWh status: {prius.kwh_status}")
prius.refuel()
prius.recharge()
print("prius.refuel()")
print("prius.recharge()")
print(f"Prius tank status: {prius.tank_status}")
print(f"Prius kWh status: {prius.kwh_status}")
