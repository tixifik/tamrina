a = input()

def r(a):
    result = []
    at = 0
    
    for i in a:
        if i == '@':
            result.append(i)
            at+=1
        elif i == '#' and at>0:
            at-=1
        else:
            result.append(i)
    return ''.join(result)
        


c = " ".join(r(a).split())
result1 = c.replace('\\n', '\n')


print(f"Formatted Text: {result1}")


