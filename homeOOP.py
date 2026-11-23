class Car :
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year  #public variable
    def get_make(self):
        return self.make
    def set_make(self, make):
        self.make = make
car = Car("とよようた", "カローラ",2049)
print (car.get_make())