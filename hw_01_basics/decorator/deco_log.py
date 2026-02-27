def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Вывод: {func.__name__}")
        print(f"Аргументы: {args},{kwargs}")
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@log_calls
def example(a,b):
    return a+b
example(2,3)