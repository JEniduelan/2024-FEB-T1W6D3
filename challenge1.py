# count vowels and consonants in a string
# count the number capital / upper case letters
# remove spaces from string without string methods

sentence = "Hello World"


num_vowels = 0
num_consonants = 0
num_upper_case = 0

for character in sentence:
    if character.isupper():
        num_upper_case += 1

    if character in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ':
        continue

    if character.lower() in "aeiou":
        num_vowels += 1
    else:
        num_consonants += 1

print(f"number of vowels: {num_vowels}")
print(f"number of consonants: {num_consonants}")
print(f"number of upper case characters: {num_upper_case}")

sentence_without_space = ""

for character in sentence:
    if character != " ":
        sentence_without_space += character

print(sentence_without_space)



