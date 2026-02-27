def sort_people_by_age(people):
    return sorted(people, key=lambda x: x['age'])

people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob',   'age': 25},
    {'name': 'Carol', 'age': 35}
]
print(sort_people_by_age(people))