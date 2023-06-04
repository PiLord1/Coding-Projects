band = input("Enter any 4-resistor color: ")
def getbandvalue(band):
    if band[0] == "K" or band[0] == "k":
        a = 0
    elif band[0] == "N" or band[0] == "n":
        a = 1
    elif band[0] == "R" or band[0] == "r":
        a = 2
    elif band[0] == "O" or band[0] == "o":
        a = 3
    elif band[0] == "Y" or band[0] == "y":
        a = 4
    elif band[0] == "G" or band[0] == "g":
        a = 5
    elif band[0] == "B" or band[0] == "b":
        a = 6
    elif band[0] == "V" or band[0] == "v":
        a = 7
    elif band[0] == "A" or band[0] == "a":
        a = 8
    elif band[0] == "W" or band[0] == "w":
        a = 9
    else:
        print("Invalid answer")
        
    if band[1] == "K" or band[1] == "k":
        b = 0
    elif band[1] == "N" or band[1] == "n":
        b = 1
    elif band[1] == "R" or band[1] == "r":
        b = 2
    elif band[1] == "O" or band[1] == "o":
        b = 3
    elif band[1] == "Y" or band[1] == "y":
        b = 4
    elif band[1] == "G" or band[1] == "g":
        b = 5
    elif band[1] == "B" or band[1] == "b":
        b = 6
    elif band[1] == "V" or band[1] == "v":
        b = 7
    elif band[1] == "A" or band[1] == "a":
        b = 8
    elif band[1] == "W" or band[1] == "w":
        b = 9
    else:
        print("Invalid answer")
    
    if band[2] == "K" or band[2] == "k":
        c = 1
    elif band[2] == "N" or band[2] == "n":
        c = 10
    elif band[2] == "R" or band[2] == "r":
        c = 100
    elif band[2] == "O" or band[2] == "o":
        c = 1000
    elif band[2] == "Y" or band[2] == "y":
        c = 10000
    elif band[2] == "G" or band[2] == "g":
        c = 100000
    elif band[2] == "B" or band[2] == "b":
        c = 1000000
    elif band[2] == "V" or band[2] == "v":
        c = 10000000
    elif band[2] == "A" or band[2] == "a":
        c = 100000000
    elif band[2] == "W" or band[2] == "w":
        c = 1000000000
    else:
        print("Invalid answer")
        
    if band[3] == "D" or band[3] == "d":
        d = 0.05
    elif band[3] == "S" or band[3] == "s":
        d = 0.10
    elif band[3] == "E" or band[3] == "e":
        d = 0.20
    else:
        print("Invalid answer")
        
    first = a*10 + b
    final = first * c
    print("Resistor value " + str(final) + " ohms")
    range1 = final - (d*final)
    x = int(range1)
    range2 = final + (d*final)
    y = int(range2)
    print("Range " + str(x) + " to " + str(y) + " ohms")
    return ""

resistor = getbandvalue(band)
print(resistor)


    

    