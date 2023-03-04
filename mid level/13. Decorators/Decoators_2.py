import functools

'''
def my_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        # DO
        res = func(*args, **kwargs)
        print('End')
        # DO
        return res

    return wrapper


@start_end_decorator
def add5(x):
    return x + 5
'''
'''
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wapper
    return decorator_repeat


@repeat(num_times=4)

def greet(name):
    print(f'Hello {name}')

greet('yash')
'''

