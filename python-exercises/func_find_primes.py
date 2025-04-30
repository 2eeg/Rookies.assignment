def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        # 1은 소수가 아님
        if num < 2:
            continue
        is_prime = True
        # 2부터 num-1까지 나누어 떨어지는지 확인
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# 테스트
start = 10
end = 30
prime_numbers = find_primes(start, end)
print(f"{start}부터 {end}까지의 소수: {prime_numbers}")