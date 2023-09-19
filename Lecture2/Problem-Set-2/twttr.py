phrase = input("Input: ")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

new_string = ""

for letter in phrase:
    if letter not in vowels:
        new_string += letter

print("Output:", new_string)