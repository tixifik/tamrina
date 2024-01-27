khaste = input()

def get_numbers():
    numbers = []
    while True:
        adad = input()
        if adad == "end":
            break
        numbers.append(float(adad))
    return numbers

def sum_numbers(numbers):
    return sum(numbers)

def average_numbers(numbers):
    return round(sum(numbers) / len(numbers), 2)

def max_number(numbers):
    return int(max(numbers))

def min_number(numbers):
    return int(min(numbers))

def gcd_numbers(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    javab = numbers[0]
    for i in range(1, len(numbers)):
        javab = gcd(numbers[i], javab)

    return int(javab)

def lcd_numbers(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    javab = numbers[0]
    for i in range(1, len(numbers)):
        javab = javab * numbers[i] / gcd(javab, numbers[i])

    return int(javab)

if khaste == "sum":
    numbers = get_numbers()
    print(sum_numbers(numbers))
elif khaste == "average":
    numbers = get_numbers()
    print(average_numbers(numbers))
elif khaste == "max":
    numbers = get_numbers()
    print(max_number(numbers))
elif khaste == "min":
    numbers = get_numbers()
    print(min_number(numbers))
elif khaste == "gcd":
    numbers = get_numbers()
    print(gcd_numbers(numbers))
elif khaste == "lcd":
    numbers = get_numbers()
    print(lcd_numbers(numbers))
else:
    print("Invalid command")
