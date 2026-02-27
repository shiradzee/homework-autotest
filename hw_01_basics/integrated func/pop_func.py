from unittest import result
def pop_until_zero(nums):
    result = []
    while nums:
        item = nums.pop()
        if item == 0:
            break
        else:
            result.append(item)
    return result
items = [10, 20, 30, 40, 50]
print(pop_until_zero(items))
