import time

def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        func(*args, **kwargs)
        end=time.time()
        print(f"execution time: {end-start}")
    return wrapper


def greet(func):
    def wrapper(*args, **kwargs):
        print(f"Hello")
        func(*args, **kwargs)
    return wrapper

@greet
@timer
def task(n):
    for i in range(1,n+1):
        print(i)

task(3)

