word = input("Enter a word: ")
start_index = int(input("Enter a index: "))

last_index = len(word)
substring = word[start_index:last_index]

print('Substring from index {}: "{}"'.format(start_index, substring))