# Base Exception Class

# Example: 2
"""
class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')


test_value(200)

"""

# Output: ValueTooHighError

# Example: 2
# including try
'''
class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')


try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
'''

# Output: value is too high

# Example: 3
# using another class
'''
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high', x)
    if x < 5:
        raise ValueTooSmallError('value is too small', x)


try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)
'''


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high', x)
    if x < 5:
        raise ValueTooSmallError('value is too small', x)


try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)
