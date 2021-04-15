#Define the running total
total = 0 

#Define the most recent input as the string
current = 0 

#Continue while current input the string x
while current !="x":

    #Convert current to an integer and add it to the total
    total = total + int(current)

    #Take a new input and set it to be the current number
    current = input("Enter a number: ")

#Convert the current to a string and print it
print(f"Your total is: {total}")