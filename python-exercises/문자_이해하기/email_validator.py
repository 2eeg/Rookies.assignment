def is_valid_email(email):
    return "@" in email and "." in email

email_addresses = ["user@example.com", "user@example", "user@.com", "example.com"]

for email in email_addresses:
    if is_valid_email(email):
        print(f"이메일 주소: {email}\n유효함")
    else:
        print(f"이메일 주소: {email}\n유효하지 않음")