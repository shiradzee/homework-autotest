def filter_even(nums):
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False
    filter_even = filter(is_even, nums)
    return list(filter_even)

print(filter_even([]))
print(filter_even([-3, -4, 0]))
print(filter_even([1, 2, 3, 4, 5, 6]))