def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called action")
        result = func(*args, **kwargs)
        print("After the function is called action")
        return result
    return wrapper

@my_decorator
def num_sum(a, b):
    x = a + b
    print(x)
num_sum(4, 3)