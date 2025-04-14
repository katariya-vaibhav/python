import time

def cache(func):
    cache_data = {}
    def wrapper(*args , **kwargs):
        start_time = time.time()
        if args in cache_data:
            print("Using cached result")
            return cache_data[args]
        result = func(*args , **kwargs)
        end_time = time.time()
        cache_data[args] = result
        print(f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result    
    return wrapper


@cache
def long_time_fun(a,b):
    time.sleep(4)
    return a + b    

print(long_time_fun(4,5))
print(long_time_fun(4,5))
print(long_time_fun(4,9))
