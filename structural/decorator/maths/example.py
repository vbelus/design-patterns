from logging_decorator import log
from validate_positive_decorator import validate_positive_numbers
from cache_decorator import cache_result

@log
@validate_positive_numbers
@cache_result
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the combined decorators
if __name__ == "__main__":
    print(fibonacci(10)) # first call
    print(fibonacci(10)) # second call, now cached
    try:
        print(fibonacci(-1))  # Will raise validation error
    except ValueError as e:
        print(e)