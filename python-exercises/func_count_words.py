def count_words(sentence):
    # 문자열을 공백 기준으로 분리하여 단어 수 계산
    words = sentence.split()
    return len(words)

# 테스트
sentence = "Python is a programming language"
word_count = count_words(sentence)
print(f"단어 수: {word_count}")