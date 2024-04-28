
def count_letters_digits(sentence):
    letters = 0
    digits = 0
    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits

sentence = input("Enter a sentence: ")
letters, digits = count_letters_digits(sentence)
print("LETTERS", letters)
print("DIGITS", digits)