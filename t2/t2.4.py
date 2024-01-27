n = int(input())
def mosalase_pascal(n):
    satr = []
    for i in range(n):
        adad = [1] * (i + 1)
        for j in range(1, i):
            adad[j] = satr[i - 1][j - 1] + satr[i - 1][j]
        satr.append(adad)
    return satr

for adad in mosalase_pascal(n):
    print(' '.join(map(str, adad)))

