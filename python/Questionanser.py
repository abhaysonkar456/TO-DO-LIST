# # class bank_account:
# #     def __init__(self, owner):
# #         self.owner = owner
# #         self._balance = 0

# #     def deposit(self, amount):
# #         if amount > 0:
# #             self._balance += amount
# #             print(f"deposited {amount}")
# #             print(f"available balance, {self._balance}")
# #         else:
# #             print("deposited amount can be positive")

# #     def withdraw(self, amount):
# #         if amount > self._balance:
# #             print("insufficent balance ")
           
# #         elif amount <= 0:
# #             print("withdraw amount can be positive")
# #         else:
# #             self._balance -= amount
# #             print(f"amount withdraw, {amount}")
# #             print(f"available balance, {self._balance}")


# # bank1 = bank_account("abhay")
# # bank1.deposit(1000)
# # bank1.withdraw(200)

# class animal:
#     def sound(self):
#         print("this animal makes sound")

# class dog(animal):
#     def sound(self):
#         print("the dog says: woof!")
# class cat(animal):
#     def sound(self):
#         print("the cat says: meow!")

# a = animal()
# d = dog()
# c= cat()

# c.sound()
# d.sound()

import math

class shape:
    def area (self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2
        
class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2

class triangle(shape):
    def __init__(self, base, height ):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
        
shapes = {circle(5), square(10), triangle(15, 7)}

for shape in shapes:
    print(f"area: { shape.area():.2f}")