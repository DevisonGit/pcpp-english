import datetime
import time


def timestamp_decorator(func):
    def wrapper(*args, **kwargs):
        # Get the current timestamp
        start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Start Timestamp: {start_time}")

        # Measure the execution time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start

        # Get the end timestamp
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"End Timestamp: {end_time}")
        print(f"Execution Time: {duration:.6f} seconds")

        return result

    return wrapper


@timestamp_decorator
def add(a, b):
    return a + b


@timestamp_decorator
def multiply(a, b):
    return a * b


# Test the decorated functions
result_add = add(3, 5)
print(f"Result of add: {result_add}")

result_multiply = multiply(4, 6)
print(f"Result of multiply: {result_multiply}")
