weight = float(input("체중(kg): "))
height_cm = float(input("키(cm): "))
height_m = height_cm / 100
bmi = weight / (height_m ** 2)
print(f"BMI: {bmi:.1f}")