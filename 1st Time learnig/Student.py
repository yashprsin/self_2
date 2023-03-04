class student:

    def __init__(self,name,f1_marks,f2_marks):
        self.name = name
        self.f1_marks = f1_marks
        self.f2_marks = f2_marks

    def passing_marks(self):
        if self.f1_marks >= 20:
            if self.f2_marks >= 20:
                print("You are passed in Science !")
                print("You are passed in Math")
            else:
                print("You are passed in Science")
                print("You are failed in Math")
        elif self.f2_marks >= 20:
            print("You are failed in Science")
            print("You are passed in Math")

        else:
            print("You failed in all subjects ")

