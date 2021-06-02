def printBoxByWidth(x):
    for row in range(5):
        for col in range(x):
            if (row == 1 and col in range(1, x - 1)) or (row == 3 and col in range(1, x - 1)):
                print(" ", end='')
            elif row == 2 and col in range(1, x - 1):
                print("o", end='')
            else:
                print("x", end='')
        print("")
        
printBoxByWidth(60)
