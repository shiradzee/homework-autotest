def sort_words_by_sorted_method(words):
    return sorted(words, key=lambda word: word.lower())

def sort_words_by_sort_method(words):
    words.sort(key=lambda word: word.lower())
    return words

sort_words = ["banana", "Apple", "cherry"]
sort_words1 = ["Kazumi","Hichigo", "Bankai"]
print(sort_words_by_sorted_method(sort_words))
print(sort_words_by_sort_method(sort_words1))