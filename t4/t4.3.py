
try:
    khatha = [input() for _ in range(6)]

    p1, p2 = khatha[0].split()
    p2 = p2.strip()

    hp1, hp2 = map(int, khatha[1].split())

    A, B, C = map(int, khatha[2].split())
    damages = {'A': A, 'B': B, 'C': C}

    p1points, p2points = 0, 0

    for i in range(3, 6):
        card1, card2 = khatha[i].split()

        if damages[card1[0]] > damages[card2[0]]:
            p1points += 1
        elif damages[card2[0]] > damages[card1[0]]:
            p2points += 1

        hp1 -= damages[card2[0]]
        hp2 -= damages[card1[0]]

    print(f"{p1} -> Score: {p1points}, Health: {hp1}")
    print(f"{p2} -> Score: {p2points}, Health: {hp2}")

except Exception as e:
    print('Invalid Command.')
    print(e)


   


    




    