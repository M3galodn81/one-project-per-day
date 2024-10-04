word = input("Enter a word: ")
print(f"{word} is a palindrome") if word[::] == word[-1::-1] else print(f"{word} is not a palindrome")
