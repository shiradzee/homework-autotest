def cache_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
    return wrapper

@cache_decorator
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b

print(slow_add(1, 2))
print(slow_add(3, 4))
print(slow_add(4, 5))
