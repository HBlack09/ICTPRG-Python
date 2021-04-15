#Telling it what to do with the inputed name
fullName = input("Full Name: ")
nameList = fullName.split(" ")

#Outputting the Initials
print("Initials: ", end="")
for i in nameList:
    print(i[0].upper(), end="")
print()