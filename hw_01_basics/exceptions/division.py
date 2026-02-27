def save_division(a,b):
    try:
        return a // b
    except ZeroDivisionError:
        return None

print(save_division(6,0))
print(save_division(6,2))

