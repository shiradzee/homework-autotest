import random
def generate_random_list(n, start, end):
    random_list = []
    for i in range(n):
        random_list.append(random.randint(start, end))
    return random_list
print(generate_random_list(5, 0, 10))