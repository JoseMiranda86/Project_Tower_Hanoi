print("\n\n\n\nWelcome to the game of the Tower of Hanoi! \n\n\n")

Counter_rounds = 0

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

 # Def of function that will define the position of the elements

    def position(n):
        count = 0
        for element in n:
            if count == 0:
                if len(element) == 9:
                    New = "       " + element
                    Newest_State.append(New)
                    A1s = len(element)
                    count = 1
                elif len(element) == 7:
                    New = "        " + element
                    Newest_State.append(New)
                    A1s = len(element)
                    count = 1
                elif len(element) == 5:
                    New = "         " + element
                    Newest_State.append(New)
                    A1s = len(element)
                    count = 1
                elif len(element) == 3:
                    New = "          " + element
                    Newest_State.append(New)
                    A1s = len(element)
                    count = 1
                else:
                    New = "           " + element
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