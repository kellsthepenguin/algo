word = input()
letters = list(word)
changed_word = ''

for letter in letters:
    if letter.islower():
        changed_word += letter.capitalize()
    else:
        changed_word += letter.lower()

print(changed_word)
