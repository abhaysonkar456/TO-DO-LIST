class Car():
    def __init__(self):
        print("mercerdecs")

    def create(self, make, model, year):
        self.made_in = make
        self.version = model
        self. default_year = year
c1 = Car()
c1.create("india", 2.0, 2025)
print("this car is made in :",c1.made_in )


