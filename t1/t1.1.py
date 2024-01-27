def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

a, b = map(int, input().split())

if 0 <= a <= 1000 and 0 <= b <= 1000:
    num1 = count_primes_in_range(min(a, b), max(a, b))
    print(f'main order - amount: {num1}' if a <= b else f'reverse order - amount: {num1}')
else:
    print("Input values must be between 0 and 1000.")
