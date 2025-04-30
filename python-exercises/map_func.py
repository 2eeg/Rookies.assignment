list1 = [1, 2, 3]
list2 = [4, 5, 6]

# map 함수와 lambda를 사용하여 두 리스트의 요소를 더하기
result = list(map(lambda x, y: x + y, list1, list2))
print(result)