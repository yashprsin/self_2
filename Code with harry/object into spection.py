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


Rohan = Emp("Rohan", "Vanes")

print(id("This is a String"))
print(id("This and That"))

print(id(Rohan))
print(dir(Rohan))
print(type(Rohan))

import inspect

print(inspect.getmembers(Rohan))
