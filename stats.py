def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lower_text = text.lower()
    letters = {}
    for l in lower_text:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters