from contextlib import contextmanager
import time
@contextmanager
def time_tracker():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Время выполнения:{end - start} сек.")

with time_tracker():
   time.sleep(1)