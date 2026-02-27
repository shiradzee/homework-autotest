def sum_all(*args):
    return sum(args)

def sum_all_modified(*args):
   return sum(args), len(args)

print(sum_all(1,2,3))
print(sum_all_modified(1, 2, 3, 4))