def normalize_whitespace(text):
    normalized_text = text.split()
    return ' '.join(normalized_text)
print(normalize_whitespace('hello     my    name    is Gustavo      Bruno'))