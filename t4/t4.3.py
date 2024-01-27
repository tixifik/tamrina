
try:

    khatha = list()

    for i in range(6):
        x = input()
        khatha.append(x)
    



    p1 ,p2 = khatha[0].split(' ')
    p2 = p2.strip()
    
    hp1 , hp2 = khatha[1].split(' ')

    hp1 = int(hp1)
    hp2 = int(hp2)

    A , B , C = khatha[2].split(' ')
    damages = {'A':A,'B':B,'C':C}

    p1points = 0
    p2points = 0
    



    for i in range(3,6):

        card1 ,card2 = khatha[i].split(' ')

        if int(damages[card1[0]]) > int(damages[card2[0]]):
            p1points += 1

        elif int(damages[card2[0]]) > int(damages[card1[0]]):
            p2points += 1

        hp1 -= int(damages[card2[0]])
        hp2 -= int(damages[card1[0]])


    print(p1 + " -> Score: "+str(p1points)+', Health: '+str(hp1))
    print(p2 + " -> Score: "+str(p2points)+', Health: '+str(hp2))
   


except:

    print('Invalid Command.')
        

   


    




    