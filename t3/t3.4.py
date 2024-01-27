def process_input(input_string):
    input_list = input_string.split()
    result_dict = {}

    for item in input_list:
        letter = item[0]
        number = item[1:]
        result_dict[number] = letter

    sorted_result = dict(sorted(result_dict.items(), key=lambda item: int(item[0])))
    result_string = ''.join(sorted_result.values())

    return result_string

def main():
    input_string = input()
    result = process_input(input_string)
    print(result)

if __name__ == "__main__":
    main()


   


    




    