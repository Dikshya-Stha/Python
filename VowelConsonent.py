string = input("Enter a string: ")
string = string.lower()  # Convert string to lowercase for case-insensitive comparison
vowels = 0
consonants = 0
for char in string:
    if char.isalpha():
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
