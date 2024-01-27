a, b=map(int,input().split())
if (a >= 0 and a <= 1000) and (b >= 0 and b <= 1000):
    num1 = 0
    if a <= b:
        if a <= 2 and b >= 2 :
            num1 += 1
        for num2 in range(a, b+1):
            primenum =0
            for i in range(2, num2):
                primenum =1
                if (num2 % i) == 0:
                    primenum =0
                    break
            if primenum == 1:
                num1 += 1
        print(f'main order - amount: {num1}')
    else: 
        if b <= 2 and a >= 2 :
                num1 += 1
        for num2 in range(b, a+1):
            primenum =0
            for i in range(2, num2):
                primenum = 1
                if (num2 % i) == 0:
                    primenum = 0
                    break
            if primenum == 1:
                num1 += 1
        print(f'reverse order - amount: {num1}')