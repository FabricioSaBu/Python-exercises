my_Word = input("Tell me your word: ")
my_Word = re.sub(r'[^a-zA-Z0-9ñÑ]', '', my_Word).lower()

# Create a reversed copy of the word using slicing
reversed_word = my_Word[::-1]

if my_Word == reversed_word:
    print(my_Word + " is a palindrome")
else:
    print(my_Word + " is not a palindrome")