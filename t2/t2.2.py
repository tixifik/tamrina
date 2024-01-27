listn=[]
listb=[]
while True:
    n, b=map(int, input().split())
    if (n ,b)==(-1 ,-1):
        break
    listn.append(int(n))
    listb.append(int(b))
    
listN= [0] * len(listn)   
for j in range(0,len(listn)):
    listN[j]=0
    for i in range(1,listn[j]+1):
        if listn[j]%i==0:
            listN[j]+=i
            
def sigma(listN,listb):
    t=0
    for k in range(0,len(listb)):
        def base(listN,listb):
            z=''
            x=listN[k]%listb[k]
            y=listN[k]//listb[k]
            while y!=0:
                z=str(x)+z
                x=y%listb[k]
                y=y//listb[k]
            z=str(x)+z
            return z     
    
        t+=int(base(listN,listb)) 
        
    return t

if all(2 <= i <= 10 for i in listb):
    print(sigma(listN, listb))
else:
    print('invalid base!')

