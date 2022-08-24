"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730545934"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) < 5 or len(user_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
user_char: str = input("Enter a single character: ")
if len(user_char) < 1 or len(user_char) > 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + user_char + " in " + user_word)

char_count: int = 0
if user_word[0] == user_char:
    char_count += 1
    print(user_char + " found at index 0")
if user_word[1] == user_char:
    char_count += 1
    print(user_char + " found at index 1")
if user_word[2] == user_char:
    char_count += 1
    print(user_char + " found at index 2")
if user_word[3] == user_char:
    char_count += 1
    print(user_char + " found at index 3")
if user_word[4] == user_char:
    char_count += 1
    print(user_char + " found at index 4")

if char_count == 0:
    print("No instances of " + user_char + " found in " + user_word)

if char_count == 1:
    print(str(char_count) + " instance of " + user_char + " found in " + user_word)
elif char_count > 1:
    print(str(char_count) + " instances of " + user_char + " found in " + user_word)
