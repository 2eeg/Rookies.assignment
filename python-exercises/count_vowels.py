text = "Python is awesome"

# 모음 리스트
vowels = ['a', 'e', 'i', 'o', 'u']

# 모음 개수 카운트
count = 0
for char in text.lower():
    if char in vowels:
        count += 1

print(f"모음 개수 : {count}")