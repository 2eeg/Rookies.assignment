id_number = "901212-1234567"

# 주민번호에서 생년월일 추출
year = id_number[0:2]
month = id_number[2:4]
day = id_number[4:6]

# 1900년대 또는 2000년대 구분 (주민번호 7번째 숫자가 1, 2는 1900년대, 3, 4는 2000년대)
if id_number[7] in ["1", "2"]:
    year = "19" + year
else:
    year = "20" + year

# 출력
print(f"{year}년 {month}월 {day}일")