from timeit import default_timer as timer
# list convert into Sting with help of For loop
My_list =['a'] * 6000000

# bad
start = timer()
Str = ""
for i in My_list:
    Str += i
# print(Str)
stop = timer()
print(stop-start)

# Good
start = timer()
Str1 =''. join(My_list)
# print(Str1)
stop = timer()
print(stop-start)

# Calculate the time


