import string

vowels = "aeiou"

user_input = input("Введите текст: ")
words = user_input.split()
pig_latin_words = []

for word in words:
    punctuation = ""
    if word and word[-1] in string.punctuation:
        punctuation = word[-1]
        word = word[:-1]

    first_letter_upper = word[0].isupper() if word else False
    word = word.lower()

    if not word:
        pig_latin_words.append(punctuation)
        continue

    if word[0] in vowels:
        pig_latin_word = word + "way"
    else:
        first_vowel_index = -1
        for i, char in enumerate(word):
            if char in vowels:
                first_vowel_index = i
                break
        if first_vowel_index == -1:
            pig_latin_word = word + "ay"
        else:
            consonants = word[:first_vowel_index]
            rest_of_word = word[first_vowel_index:]
            pig_latin_word = rest_of_word + consonants + "ay"

    if first_letter_upper:
        pig_latin_word = pig_latin_word[0].upper() + pig_latin_word[1:]

    pig_latin_words.append(pig_latin_word + punctuation)

print(" ".join(pig_latin_words))