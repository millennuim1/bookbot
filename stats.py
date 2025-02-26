def get_num_words(text):
    words = text.split()
    return len(words)

def count_Characters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
                char_counts[char] += 1
        else:
             char_counts[char] = 1
    return char_counts

def sort_on(dict):
     return list(dict.values())[0]
        