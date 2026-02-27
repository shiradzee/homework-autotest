def multiple_exceptions_handling(key1, key2):
    data = {"x": "10", "y": "0", "z": "abc"}
    try:
        value1 = data[key1]
        value2 = data[key2]
        num1 = int(value1)
        num2 = int(value2)
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Division by zero")
    except KeyError as e:
        print(f"KeyError: ключ {e} не найден")
    except ValueError:
        print("ValueError")
    else:
        print("Ошибок не обнаружено")
    finally:
        print("Completed")

print(multiple_exceptions_handling("y", "x"))
print(multiple_exceptions_handling("x", "y"))
print(multiple_exceptions_handling("x", "z"))

