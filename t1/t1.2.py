def decimal_to_binary(number):
    return "{:032b}".format(number)

def check_bit(binary_string, position):
    return binary_string[-position - 1]

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    
    binary_a = str(decimal_to_binary(a))
    binary_b = str(decimal_to_binary(b))
    
    binary_result = binary_b + binary_a
    
    results_list = []
    
    for _ in range(c):
        input_value = int(input())
        if check_bit(binary_result, input_value) == '1':
            results_list.append('yes')
        elif check_bit(binary_result, input_value) == '0':
            results_list.append('no')
    
    for result in results_list:
        print(result)

if __name__ == "__main__":
    main()




