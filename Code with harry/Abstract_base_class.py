"""
from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(shape):
    type = "Rectangle"
    side = 4

    def __init__(self):
        self.len = 4
        self.wid = 2

    def print_area(self):
        return self.len * self.wid


rect = Rectangle()
print(rect.print_area())
"""


# ---------------- setter and property decorator --------------

class Emp:

    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    def print_name(self):
        return f"Employee name is {self.fn} {self.ln}"

    @property
    def email(self):
        if self.fn is None or self.ln is None:
            return "email deleted successfully"
        return f"{self.fn}.{self.ln}@uCasting.com"

    @email.setter
    def email(self, string):
        print("Update Successful")
        name = string.split("@")[0]
        self.fn = name.split(".")[0]
        self.ln = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fn = None
        self.ln = None


tom = Emp("Tom", "Curse")

print(tom.print_name())
print(tom.email)

tom.fn = "King"
print(tom.email)

tom.email = "this.that@uCasting.com"
print(tom.fn)
print(tom.ln)
print(tom.email)

del tom.email
print(tom.email)
