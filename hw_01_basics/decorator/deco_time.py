import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.4f} сек.")
        return result
    return wrapper

@timer
def time_task():
    time.sleep(1)
    print("test")
time_task()
