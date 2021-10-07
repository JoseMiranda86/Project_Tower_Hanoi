import os

clear = lambda: os.system('cls')

print("\n\n\n\nWelcome to the game of the Tower of Hanoi! \n\n\n")

Counter_rounds = 0
min = (2**4)-1

# Defining the inial state of the grid
data = {'A1':"s", 'A2':"000", 'A3':"00000",
        'A4':"0000000", 'A5':"000000000",
        'B1':"s", 'B2':"s", 'B3':"s", 'B4':"s",
        'B5':"s", 'C1':"s", 'C2':"s", 'C3':"s",
        'C4':"s", 'C5':"s"}

# Start loop of game
while True:
# Definition of list that will contain the most recent state
    Newest_State= list()
# Definition of each line of the grid as a list of values    
    Line1 = [data['A1'], data['B1'], data['C1']]
    Line2 = [data['A2'], data['B2'], data['C2']]
    Line3 = [data['A3'], data['B3'], data['C3']]
    Line4 = [data['A4'], data['B4'], data['C4']]
    Line5 = [data['A5'], data['B5'], data['C5']]

 # Function that will define the position of the elements

    def position(n):
        count = 0
        for element in n:
            if count == 0:
                if len(element) == 9:
                    New = " "*7 + element
                    Newest_State.append(New)
                    A1s = len(element)
                    count = 1
                elif len(element) == 7:
                    New = " "*8 + element
                    Newest_State.append(New)
                    A1s = len(element)
                    count = 1
                elif len(element) == 5:
                    New = " "*9 + element
                    Newest_State.append(New)
                    A1s = len(element)
                    count = 1
                elif len(element) == 3:
                    New = " "*10 + element
                    Newest_State.append(New)
                    A1s = len(element)
                    count = 1
                else:
                    New = " "*11 + element
                    Newest_State.append(New)
                    A1s = len(element)
                    count = 1

            elif count == 1:
                if len(element) == 9:
                    New = int(13 - ((A1s-1)/2))* " " + element
                    Newest_State.append(New)
                    B1s = len(element)
                    count = 2
                elif len(element) == 7:
                    New = int(14 - ((A1s-1)/2))* " " + element
                    Newest_State.append(New)
                    B1s = len(element)
                    count = 2
                elif len(element) == 5:
                    New = int(15 - ((A1s-1)/2))* " " + element
                    Newest_State.append(New)
                    B1s = len(element)
                    count = 2
                elif len(element) == 3:
                    New = int(16 - ((A1s-1)/2))* " " + element
                    Newest_State.append(New)
                    B1s = len(element)
                    count = 2
                else:
                    New = int(17 - ((A1s-1)/2))* " " + element
                    Newest_State.append(New)
                    B1s = len(element)
                    count = 2
            else:
                if len(element) == 9:
                    New = int(13 - ((B1s-1)/2))* " " + element
                    Newest_State.append(New)
                    C1s = len(element)
                elif len(element) == 7:
                    New = int(14 - ((B1s-1)/2))* " " + element
                    Newest_State.append(New)
                    C1s = len(element)
                elif len(element) == 5:
                    New = int(15 - ((B1s-1)/2))* " " + element
                    Newest_State.append(New)
                    C1s = len(element)
                elif len(element) == 3:
                    New = int(16 - ((B1s-1)/2))* " " + element
                    Newest_State.append(New)
                    C1s = len(element)
                else:
                    New = int(17 - ((B1s-1)/2))* " " + element
                    Newest_State.append(New)
                    C1s = len(element)  

# Def function to print latest state of grid
    def TowerState(A1, A2, A3, A4, A5, B1, B2, B3, B4, B5, C1, C2, C3, C4, C5) :
        print("             A                 B                 C\n")
        print("1-"+A1+B1+C1)
        print("2-"+A2+B2+C2)
        print("3-"+A3+B3+C3)
        print("4-"+A4+B4+C4)
        print("5-"+A5+B5+C5+"\n\n")

    def positions():
        position(Line1)
        position(Line2)
        position(Line3)
        position(Line4)
        position(Line5)    

# Checking status of grid.Calling function to define new positions


    positions()
    TowerState(Newest_State[0], Newest_State[3], Newest_State[6], Newest_State[9], Newest_State[12], Newest_State[1], Newest_State[4], Newest_State[7], Newest_State[10], Newest_State[13], Newest_State[2], Newest_State[5], Newest_State[8], Newest_State[11], Newest_State[14])

    if len(data['B5']) > len(data['B4']) and len(data['B4']) > len(data['B3']) and len(data['B3']) > len(data['B2']) and len(data['B2']) > len(data['B1']):
        print("\n\n\n\n\n\n    CONGRATULATIONS!!!\n  YOU SOLVED THE PUZZLE!\n\n\n\nYou solved the puzzle in "+str(Counter_rounds)+" moves\n\nThe min number of moves for this puzzle is "+str(min)+"\n\n\n\n")
        break
    elif len(data['C5']) > len(data['C4']) and len(data['C4']) > len(data['C3']) and len(data['C3']) > len(data['C2']) and len(data['C2']) > len(data['C1']):
        print("\n\n\n\n\n\n    CONGRATULATIONS!!!\n  YOU SOLVED THE PUZZLE!\n\n\n\nYou solved the puzzle in "+str(Counter_rounds)+" moves\n\nThe min number of moves for this puzzle is "+str(min)+"\n\n\n\n")
        break
    else:
        x = 1

    while True:
        level= input("Choose the column origin: ")
        dataOri = level.upper()
        if dataOri != "A" and dataOri != "B" and dataOri != "C":
            print("\nPlease choose a valid column\n\n")
            continue
        else:
            break

    print("\n")

    while True:
        Newlevel = input("Choose the column destination: ")
        dataDes = Newlevel.upper()
        if dataDes != "A" and dataDes != "B" and dataDes != "C":
            print("\nPlease choose a valid column\n\n")
            continue
        elif dataDes == dataOri:
            print("\nPlease choose a different column for the destination\n\n")
            continue
        else:
            break

    clear()        

    print("\n")

    for i in [1, 2, 3, 4, 5]:
        count = i
        n = data[dataOri+str(i)]
        if count < 5 and len(n) > 1:
            var1 = n
            keyO = dataOri+str(i)
            break
        elif len(n) > 1:
            var1 = n
            keyO = dataOri+str(i)
            break
        else:
            var1 = "s"
            keyO = dataOri+str(i)

    for i in [1, 2, 3, 4, 5]:
        count = i
        m = data[dataDes+str(i)]
        if count < 5 and len(m) > 1:
            var2 = m
            keyD = dataDes+str(i)
            keyD2 = dataDes+str(i-1)
            break
        elif len(m) > 1:
            var2 = m
            keyD = dataDes+str(i)
            keyD2 = dataDes+str(i-1)
            break
        else:
            var2 = "s"
            keyD = dataDes+str(i)
            keyD2 = dataDes+str(i-1)

    if len(var2) == 1:
        newvalue1 = data[keyO]
        newvalue2 = data[keyD]
        data[keyO] = newvalue2
        data[keyD] = newvalue1
        Counter_rounds = Counter_rounds + 1

    elif len(var2) > len(var1) and len(var2) > 1:
        newvalue1 = data[keyO]
        newvalue2 = data[keyD2]
        data[keyO] = newvalue2
        data[keyD2] = newvalue1
        Counter_rounds = Counter_rounds + 1

    else:
        print("\n\nCAN'T MOVE!!!!!\nThe size of the disk at the origin is bigger than the one at the destination! \n\n\n")
        Counter_rounds = Counter_rounds + 1
        continue   