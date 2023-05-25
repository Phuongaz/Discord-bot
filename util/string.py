from collections import Counter

def find_most_common_strings(strings):
    word_counts = Counter(strings)
    
    most_common_strings = [(word, count) for word, count in word_counts.items() if len(word) > 1]
    most_common_strings.sort(key=lambda x: x[1], reverse=True)
    
    return most_common_strings