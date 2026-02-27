def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def greet_modified(**kwargs):
    if "name" in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello!")

greet(name = "john", age = 25)
greet_modified(name = "john", age = 25)
greet_modified(city ="Moscow", age = 25)
