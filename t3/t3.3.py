def m():
    n = int(input())
    payam = {}    

    for i in range(n):
        email = input()
        if '@' in email:
            a = t(email)  
            payam[a] = 1 

    sorted_a = sorted(payam.keys())

    for a in sorted_a:
        print(a)

def t(email):
    return email.split('@')[-1]

m()

