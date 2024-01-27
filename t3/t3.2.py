a = input()
b = int(input())
x = a.split()
dict_x = {}

for i, num in enumerate(x):
    dict_x[int(num)] = i

dict_m = {}

for j in dict_x.keys():
    c = b - j
    if c in dict_x and c != j:
        d = dict_x[j] + dict_x[c]
        if (c, j) not in dict_m.keys():
            dict_m[(j, c)] = d

if not dict_m:
    print("Not Found!")
else:
    for h in sorted(dict_m.values()):
        print(h)



