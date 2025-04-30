def validate_email(email):
    # '@'와 '.'가 모두 포함되어 있는지 확인
    return '@' in email and '.' in email

# 유효한 이메일 테스트
email1 = "user@example.com"
print(f"이메일 주소: {email1}")
if validate_email(email1):
    print("유효함")
else:
    print("유효하지 않음")

# 유효하지 않은 이메일 테스트
email2 = "user@example"
print(f"이메일 주소: {email2}")
if validate_email(email2):
    print("유효함")
else:
    print("유효하지 않음")