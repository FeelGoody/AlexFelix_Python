from collections import Counter

def top_word(x):
    print(Counter(x.lower().split()).most_common(1))

top_word ("Hello World Hello Hello World World World")
# print(Counter(words).most_common(2))
