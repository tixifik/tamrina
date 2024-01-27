x = input()
x_list = x.split()

result = {}

for i in x_list:
    letter = i[0]   
    number = i[1:]
    result[number] = letter

sorted_result = dict(sorted(result.items(), key=lambda item: int(item[0])))

a = ''.join(sorted_result.values())
print(a)

   


    




    