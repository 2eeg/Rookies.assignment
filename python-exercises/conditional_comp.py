numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num**2 if num % 2 == 0 else num for num in numbers]
print(result)