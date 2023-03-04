# Exception case

"""
x = 5
if x > 0:
    raise Exception('x is should be positive.')
"""

# AssertionError
'''
x = -5
assert (x >= 0), 'x should be positive'
'''
# Zero Division Error
'''
a = 5/0
'''

# Try and expect blog
'''
try:
    a = 5/0
except:
    print('an error happened')
'''
# try and exception
# Example 1
'''
try:
    a = 5/0
except Exception as e:
    print(e)
'''
# showing division by zero

# Example 2
'''
try:
    a = 5/0
except ZeroDivisionError as e:
    print(e)
'''
# Output : ZeroDivisionError

# Example 3
'''
try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
'''
# Output : unsupported operand type(s) for +: 'float' and 'str'

# Example 4
'''
try:
    a = 5 / 0
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
'''
# Output : ZeroDivisionError

# Example 5
'''
try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is Fine")
'''
# Output: Everything is fine

# Example 6
'''
try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is Fine")
finally:
    print('Cleaning up...')

Output:
Everything is Fine
Cleaning up...
'''