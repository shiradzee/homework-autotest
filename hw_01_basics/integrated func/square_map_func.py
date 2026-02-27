def squares_map(nums):
    def square(num):
        return num ** 2
    return list(map(square, nums))

print(squares_map([1, 2, 3, 4, 5]))

print(squares_map([]))

print(squares_map([-2, -1, 0, 1, 2]))