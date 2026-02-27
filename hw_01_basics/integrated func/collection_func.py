from collections import Counter
def count_word_frequencies(words):
    counter = Counter(words)
    return counter

print(count_word_frequencies([
    "apple", "banana", "apple", "orange", "banana", "apple"]))


