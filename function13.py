#Write a Python function total number of  Combinations:

def count_lowercase_and_uppercase_letters(s):
    lowercase_count = 0
    uppercase_count = 0
    for char in s:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1

    return lowercase_count, uppercase_count

string = "STatiStiCS"
lowercase_count, uppercase_count = count_lowercase_and_uppercase_letters(string)
print(f"Lowercase letters: {lowercase_count}")
print(f"Uppercase letters: {uppercase_count}")

