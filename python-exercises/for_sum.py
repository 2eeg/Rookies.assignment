total = 0
for num in range(1, 101):
    if num % 3 == 0:
        total += num
print(f"3의 배수의 합: {total}")