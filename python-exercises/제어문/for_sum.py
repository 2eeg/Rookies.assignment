# File: /python-exercises/python-exercises/제어문/for_sum.py

total_sum = sum(i for i in range(1, 101) if i % 3 == 0)
print(f"3의 배수의 합: {total_sum}")