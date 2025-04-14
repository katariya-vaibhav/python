import time

def timer(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        Result = func(*args , **kwargs)
        end = time.time()
        print(f"{func.__name__} Function Execution time: {end - start:.4f} seconds")
        return Result
    return wrapper


@timer
def example(n):
    time.sleep(n)
    return n

example(4)