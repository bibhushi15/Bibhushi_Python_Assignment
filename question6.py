word = input("Enter a word:")

first_word = word[0]
last_word = word[len(word) - 1]
middle_part = word[1:len(word) - 1]

new_word = last_word + middle_part + first_word

print(new_word)