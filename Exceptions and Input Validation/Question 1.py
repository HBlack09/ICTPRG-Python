while True:
    try:
        InputNumber = int(input("Please enter a number: "))
        if InputNumber == 77:
            print("That was the valid number")
            print(InputNumber)
            break
    except WrongNumber:
        print("Sorry, that is not the valid number. Try again!")
