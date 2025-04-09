# File: /python-exercises/python-exercises/문자_이해하기/count_vowels.py

# This file counts the number of vowels in the string "Python is awesome" and prints the result.

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in text if char in vowels)
    return count

if __name__ == "__main__":
    text = "Python is awesome"
    vowel_count = count_vowels(text)
    print(f"모음 개수 : {vowel_count}")