# -----------------class function----------------------
"""
class Student:
    pass

harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 1
larry.subject = ["hindi", "English"]
print(harry.name, larry.subject)
"""
# -------------------class function print return value----------------------
"""
class Emp:
    no_of_leaves = 8

    def print_derails(self):
        return f"\n Name is {self.name}.\n Salary is {self.salary}.\n and role is {self.role}."


harry = Emp()
larry = Emp()

harry.name = "Harry"
harry.salary = 122
harry.role = "Student"

larry.name = "Larry"
larry.salary = 122
larry.role = "Instructor"

print(larry.print_derails())
"""
# -------------------class method ----------------------
"""
class Emp:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_derails(self):
        return f"\n Name is {self.name}.\n Salary is {self.salary}.\n and role is {self.role}."

    @classmethod
    def change_leave(cls, nwl):
        cls.no_of_leaves = nwl


harry = Emp("Harry", 455, "Student")
rohan = Emp("Rohan", 4999, "Instructor")

harry.no_of_leaves = 12
print(harry.no_of_leaves)
"""
# -------------------class method using split sting----------------------
"""

class Emp:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_derails(self):
        return f"\n Name is {self.name}.\n Salary is {self.salary}.\n and role is {self.role}."

    @classmethod
    def change_leave(cls, nwl):
        cls.no_of_leaves = nwl

    #
    # @classmethod
    # def from_str(cls, string):
    #     pr = string.split("-")
    #     return cls(pr[0], pr[1], pr[2])

    # in one line
    @classmethod
    def fr_st(cls, string):
        return cls(*string.split("-"))


harry = Emp("Harry", 455, "Student")
rohan = Emp("Rohan", 4999, "Instructor")
karan = Emp.fr_st("karan-239-Student")

print(karan.salary)
"""


# -------------------class method in one line using split method----------------------
"""
class Emp:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_derails(self):
        return f"\n Name is {self.name}.\n Salary is {self.salary}.\n and role is {self.role}."

    @classmethod
    def change_leave(cls, nwl):
        cls.no_of_leaves = nwl

    # @classmethod
    # def from_str(cls, string):
    #     pr = string.split("-")
    #     return cls(pr[0], pr[1], pr[2])

    # in one line
    @classmethod
    def fr_st(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def pr(string):
        print("This is good " + string)


harry = Emp("Harry", 455, "Student")
rohan = Emp("Rohan", 4999, "Instructor")
karan = Emp.fr_st("karan-239-Student")

print(karan.salary)
karan.pr("harry")
"""
# -------------------abstraction and encapsulation----------------------
