# Build a shopping list
print("Enter")
# Display message to user
print("Hi! Please enter an item for the shopping list")
print("Enter x to finish the list")
#Initialise variables
shoppinglist=[]
userInput = ""
#Accept user input
while (True):
    userInput = input("Enter Item: ")
    print("userInput:",userInput)
    if userInput == "x":
        break
   
    shoppinglist.append(userInput)
    print("Your shopping list is " +str(shoppinglist))
