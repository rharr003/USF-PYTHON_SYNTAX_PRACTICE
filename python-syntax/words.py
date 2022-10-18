def print_upper_words(words, criteria):
    result = ''
    for word in words:
        if word[0].lower() in criteria:
            result += f'{word.title()}\n'
    return result

print(print_upper_words(['hello', 'bye', 'sorry', 'eggs'], ['h', 'e']))