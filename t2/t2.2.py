def get_divisors_sum(number):
    return sum(i for i in range(1, number + 1) if number % i == 0)

def convert_to_base(n, base):
    result = ''
    while n != 0:
        result = str(n % base) + result
        n //= base
    return result

def main():
    list_n = []
    list_b = []

    while True:
        n, b = map(int, input().split())
        if (n, b) == (-1, -1):
            break
        list_n.append(n)
        list_b.append(b)

    list_N = [get_divisors_sum(n) for n in list_n]

    def sigma(list_N, list_b):
        total = 0
        for k in range(len(list_b)):
            total += int(convert_to_base(list_N[k], list_b[k]))
        return total

    if all(2 <= i <= 10 for i in list_b):
        print(sigma(list_N, list_b))
    else:
        print('Invalid base!')

if __name__ == "__main__":
    main()

