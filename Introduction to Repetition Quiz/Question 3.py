#Define the number --> the users input
number = int(input("Enter a number: "))

#Keep asking for input while the number is between 50 and 70
while not(number in range(50,71)):
    print(f"{number} is not within the given range.")
    number = int(input("Enter a number: "))

#Tell the user when a number is within defined range
print(f"{number} is within the given range.")