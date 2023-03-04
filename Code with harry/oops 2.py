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


class Programmer(Emp):
    no_of_holidays = 56

    def __init__(self, name, salary, role, language):
        super().__init__(name, salary, role)
        self.language = language

    def print_derails2(self):
        return f"\n Name is {self.name}.\n Salary is {self.salary}.\n and role is {self.role} .\n The language is{self.language}"


harry = Emp("Harry", 455, "Student")
rohan = Emp("Rohan", 4999, "Instructor")
karan = Emp.fr_st("karan-239-Student")

shubham = Programmer("Shubham", 555, "Programmer", ["Python"])
Tommy = Programmer("Tommy", 695, "Programmer", ["Python"])

print(shubham.no_of_holidays)
"""

"""
class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Player:
    var = 9
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"


class CoolProgramer(Employee, Player):
    language = "C++"

    def printlanguage(self):
        print(self.language)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgramer("Karan", 8778, "gvgjkjij")
det = karan.printdetails()
karan.printlanguage()
print(det)
print(karan.var)
"""

# --------------multi level inheritance ------------------
"""
class dad:
    baseket_ball = 1


class son(dad):
    dance = 1

    def Is_dance(self):
        return f"Yes I dance {self.dance} no. of Times !"


class Grand_son(son):
    dance = 6
    

daddy = dad()
larry = son()
harry = Grand_son()

print(dad.baseket_ball)
print(larry.dance)
print(larry.Is_dance())
print(harry.Is_dance())
"""

# -----------------quiz------------------------
"""
class Electronic_Device:
    Definition = "According to Statista, there are about 21.5 billion interconnected devices in the world."
    electronic = 9


class Pocket_Gadget(Electronic_Device):
    Definition = "A small specialized mechanical or electronic device; a contrivance."
    pock_dev = 7

    def used(self):
        return f" My pocket gadget used {self.electronic} electronic device."


class Phone(Pocket_Gadget):
    Definition = "A mobile phone, cellular phone, cell phone, cellphone, headphones, or hand phone, sometimes " \
                 "shortened to simply mobile, cell or just phone, is a portable telephone that can make and receive " \
                 "calls over a radio frequency link while the user is moving within a telephone service area. "

    def used(self):
        return f" My pocket gadget used {self.electronic} electronic device." \
                f"I using in my phone {self.pock_dev} pocket devices !"




ph = Phone()
print(ph.used())
"""

# ---------------------- oops 11 ----------------------------------
"""
class A:
    Class_var1 = "I am class variable 1 in class A"

    def __init__(self):
        self.var1 = " I am inside class A's Constructor"
        self.Class_var1 = " I am instance var in class A"
        self.special  = "Special"


class B(A):
    Class_var1 = "I am class variable in class B"

    def __init__(self):

        self.var1 = " I am inside class B's Constructor"
        self.Class_var1 = " I am instance var in class B"
        print(super().Class_var1)
        super().__init__()


a = A()
b = B()

print(b.special, b.var1, b.Class_var1)
"""

# ------------------------ Diamond shape -------------------
"""
class A:
    def met(self):
        print("This is method of class A ")


class B(A):
    def met(self):
        print("This is method of class B ")


class C(A):
    def met(self):
        print("This is method of class C ")


class D(B, C):
    def met(self):
        print("This is method of class D ")


d = D()
d.met()
"""


# ----------------------------- Dunder method and operator overloading---------------------
class Emp:
    nol = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"The name is {self.name}. Salary is {self.salary}. Role is {self.role}"

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return self.print_details()

    def __str__(self):
        return f"Employee - {self.name} - {self.role} - {self.salary}"


emp_1 = Emp("Rohan", 787, "Programmer")
emp_2 = Emp("Karan", 87, "Cleaner")

print(emp_1 + emp_2)
print(emp_1 / emp_2)
print(emp_1)