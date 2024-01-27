a=int(input())
b=input()
c=input()
listb=[]
for x in b:
    if x not in['ØŒ' ,'.',':']:
        listb.append(x)
        
s="".join(i for i in listb)
list1=s.split()
list2=[]
for x in list1:
    if len(x)==len(c):
        m=len(x)
    elif len(x)>len(c):
        c = c.ljust(len(x), "_")
        m=len(x)
    elif len(c)>len(x):
        x = x.ljust(len(c), "_")
        m=len(c)
        
    for i in range(len(c)):
        if c[i]==x[i]:
            m-=1
    if m in range(a+1):
        list2.append(x)
        
for k in list2:
    k = k.replace("_","")
    print(k)
