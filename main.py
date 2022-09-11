letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZab" \
          "cdefghijklmnopqrstuvwxyz"


def unique_english_letters(word):
    letter_counter = 0

    for letter in letters:
        if letter in word:
            letter_counter += 1

    return letter_counter


print(unique_english_letters("mississippi"))

print(unique_english_letters("Apple"))
