satr=[]
makan=[]
i = 0
j = 0
n = int(input())
for x in range(n):
    satr.append('.')
    
for x in range(1000):
    y=satr.copy()
    makan.append(y)
makan[i][j]='*'
c=input()

while c!="END":

    if c=="R":
        if j < n-1:
            j+=1
        else:
            j = n-1
    elif c=="L":
         if j-1>=0:
             j-=1
         else:
             j=0        
    elif c=="B":
        i +=1
    makan[i][j]='*'
    c=input()


while True:
    
    if satr in makan:
        makan.pop(makan.index(satr))
    else:
        break

for k in range(len(makan)):
    for K in range(n):
        print(makan[k][K],end=' ')
    print('\n')

if j != n-1:
    print("There's no way out!")
