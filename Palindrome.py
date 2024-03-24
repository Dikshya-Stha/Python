string = input("Enter a string: ")


string_lower = string.lower()


if string_lower == string_lower[::-1]:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
