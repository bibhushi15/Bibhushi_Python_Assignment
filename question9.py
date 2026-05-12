sentence = input("Enter a sentence: ")

words = sentence.split(" ")
new_sentence = ""

for i in range(len(words)):
    if i % 2 == 1:
        word = words[i]
        reversed_word = word[len(word)::-1]
        new_sentence += reversed_word
    else:
        new_sentence += words[i]

    if i != len(words) - 1:
        new_sentence += " "

print(new_sentence)