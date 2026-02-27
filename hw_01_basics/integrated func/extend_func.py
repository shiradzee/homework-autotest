def merge_lists_by_extend(a,b):
    a.extend(b)
    return a
def merge_lists_without_extend(a,b):
    return a + b
print(merge_lists_by_extend([1,2,3,4,5],[6,7,8,9,10]))