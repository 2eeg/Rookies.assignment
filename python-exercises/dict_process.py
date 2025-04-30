# {"name": "John", "age": 30} 딕셔너리에서 "age"의 값 출력
person = {"name": "John", "age": 30}
print(f"나이: {person['age']}")

# {"math": 90, "science": 85, "history": 78} 딕셔너리에서 모든 과목명 출력
grades = {"math": 90, "science": 85, "history": 78}
subjects = list(grades.keys())
print(f"과목들: {subjects}")

# {'apple': 3, 'banana': 5}에서 apple의 값을 2 증가시키기
fruits = {'apple': 3, 'banana': 5}
fruits['apple'] += 2
print(fruits)