"""
def dec1(func):
    def now():
        print("Hello")
        func()
        print("Exit")

    return now

@dec1
def func():
    print("yash")


# func = dec1(func)
func()
"""
