class Car:
    runs = True
    number_of_wheels=4
    def __init__(self, name):
        print("hgello")
        self.name = name
    def __str__(self):
        return f"My car {self.name} currently {self.runs}"
    def __repr__(self):
        return f"Car {self.name}"
    def start(self):
        if self.runs:
            print(f"{self.name} CArs started")
        else:
            print(f"car is {self.name} broken")
    @classmethod
    def get_wheels(cls):
        return cls.number_of_wheels