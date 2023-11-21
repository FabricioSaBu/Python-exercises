def solution(first_word, second_word):
    if sorted(first_word) == sorted(second_word):
        print("your words are anagrams")
    else:
        print("Your words are not anagrams")

solution("tomato", "tomate")