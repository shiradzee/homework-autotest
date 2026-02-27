def squeare_odds(nums):
    odds = filter(lambda x: x % 2 != 0, nums)
    squared = map(lambda x: x ** 2, odds)
    return list(squared)
print(squeare_odds([1, 2, 3, 4, 5, 6]))