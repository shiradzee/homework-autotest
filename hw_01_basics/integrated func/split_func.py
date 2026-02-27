def count_words(text):
    words = text.strip().split()
    return len(words)
print(count_words('hello! My name is Gustavo Bruno'))
