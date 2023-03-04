# lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5))

# Similar function
def add10_func(x):
    return x+10

# Second example
mult = lambda x,y: x+y
print(mult(2,7))

point2D = [(1,2),(15,1),(5,-1),(10,4)]
point2D_sorted = sorted(point2D)

print(point2D)
print(point2D_sorted)

# but there is problem they can't sorted y of the list
point2D_sorted_lambda = sorted(point2D, key=lambda x: x[1])
print(point2D_sorted_lambda)

# similar function
'''def sort_by_y(x):
    return x[1]

'''
# sum of each
point2D_sorted_lambda_2 = sorted(point2D, key=lambda x: x[0]+ x[1])
print(point2D_sorted_lambda_2)
