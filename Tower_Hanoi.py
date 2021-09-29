print("\n\n\n\nWelcome to the game of the Tower of Hanoi! \n\n\n")

Counter_roundes = 0

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