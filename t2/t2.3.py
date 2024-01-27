khaste=input()
if khaste=="sum":
    numbers = []
    x = 0
    while True:
        adad = input()
        if adad == "end":
            break
        numbers.append(int(adad))
    for i in range(len(numbers)):
        x+=numbers[i]
    print(x)
elif khaste=="average":
    numbers = []
    x=0
    while True:
        adad = input()
        if adad == "end":
            break
        numbers.append(float(adad))
    for i in range(len(numbers)):
        x+=numbers[i]        
    miangin= x/len(numbers) 
    print(round( miangin,2 ))
    
elif khaste=="max":
    numbers = []
    while True:
        adad = input()
        if adad == "end":
            break
        numbers.append(float(adad))
    Max=max(numbers)
    print(int(Max))  
    
elif khaste=="min" :
    numbers = []
    while True:
        adad = input()
        if adad == "end":
            break
        numbers.append(float(adad))
    Min=min(numbers)
    print(int(Min))  
    
elif khaste=="gcd" :
    numbers = []
    while True:
        adad = input()
        if adad == "end":
            break
        numbers.append(int(adad))
    def gcd_numbers(numbers):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
         
        javab=numbers[0]    
        for i in range(1,len(numbers)):
            javab=gcd(numbers[i],javab)
            
        return javab 

    print(int(gcd_numbers(numbers)))
        
elif khaste=="lcd":
    numbers = []
    while True:
        adad = input()
        if adad == "end":
            break
        numbers.append(int(adad))
        
    def lcd(numbers):
        def gcd(a, b):
            while b:
                 a, b = b, a % b
            return a
        javab=numbers[0]
        for i in range(1,len(numbers)):
            javab= javab*numbers[i]/gcd(javab,numbers[i])
            
        return javab

    print(int(lcd(numbers)))
    
else:
    print("Invalid command")    