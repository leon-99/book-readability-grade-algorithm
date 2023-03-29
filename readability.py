def main():
    text = input("Text: ").strip()

    letters = count_letters(text)
    words = count_words(text)
    setences = count_setences(text)

    # calculating the averages per 100 words
    L = letters / words * 100
    S = setences / words * 100

    # calculating the grade
    index = round((0.0588 * L) - (0.296 * S) - 15.8)

    # printing the result
    if index < 1:
        print()
        print("Before Grade 1")
    elif index > 16:
        print()
        print("Grade 16+")
    else:
        print()
        print(f"Grade {index}")


def count_letters(text):
    letters = 0
    for c in text:
        if c.isupper() or c.islower():
            letters += 1
    return letters


def count_words(text):
    words = 0
    for c in text:
        if c.isspace():
            words += 1
    return words + 1


def count_setences(text):
    setences = 0
    for c in text:
        if c == "." or c == "?" or c == "!":
            setences += 1
    return setences


main()
