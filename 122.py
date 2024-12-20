vowels = "aeiou"

user_input = input("Введите текст: ").lower()
words = user_input.split()
pig_latin_words = []

for word in words:
    if word[0] in vowels:
        pig_latin_words.append(word + "way")
    else:
        first_vowel_index = -1
        for i, char in enumerate(word):
            if char in vowels:
                first_vowel_index = i
                break
        if first_vowel_index == -1:
            pig_latin_words.append(word + "ay")
        else:
            consonants = word[:first_vowel_index]
            rest_of_word = word[first_vowel_index:]
            pig_latin_words.append(rest_of_word + consonants + "ay")

print(" ".join(pig_latin_words))