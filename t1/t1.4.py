def decimal_to_binary(number, length=100):
    return int(format(number, f'0{length}b'))

a = int(input())
b = int(input())

binary_a = decimal_to_binary(a)
binary_b = decimal_to_binary(b)

c = 0

for i in range(100):
    c += abs((binary_a // 10**i) % 2 - (binary_b // 10**i) % 2)

print(c)
