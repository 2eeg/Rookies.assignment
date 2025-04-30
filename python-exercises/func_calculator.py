def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "0으로 나눌 수 없습니다."
    else:
        return "잘못된 연산자입니다."

# 테스트
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # 문제 예시 출력값

# 다양한 연산 테스트 코드 (주석 처리)
"""
print(calculator(5, 3, '+'))  # 8
print(calculator(5, 3, '-'))  # 2
print(calculator(5, 3, '*'))  # 15
print(calculator(6, 3, '/'))  # 2.0
print(calculator(5, 0, '/'))  # 0으로 나눌 수 없습니다.
print(calculator(5, 3, '%'))  # 잘못된 연산자입니다.
"""