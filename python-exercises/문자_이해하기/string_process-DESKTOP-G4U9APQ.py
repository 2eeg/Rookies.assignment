hello = "Hello"
world = "World"

# 1. "Hello"와 "World" 연결하기
greeting = hello + " " + world
print(greeting)

# 2. 대문자로 변환하기
print(greeting.upper())

# 3. "Hello World"에서 "World" 슬라이싱하기
print(greeting[6:])

# 4. "Python is fun"을 공백으로 분리하기
split_string = "Python is fun".split()
print(split_string)

# 5. "abcdef"에서 짝수 인덱스 문자 추출하기
even_index_chars = "abcdef"[::2]
print(even_index_chars)

# 6. "Hello"를 세 번 반복하기
print(hello * 3)