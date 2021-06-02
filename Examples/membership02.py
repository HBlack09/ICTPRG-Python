age = int( input("Enter age: "))
hasMem = input("Do you have membership y or Y? ")
hasMembership = (hasMem == "Y" or hasMem == "y")
#age = 2
#hasMembership=False
if (hasMembership == True):
    if (age >= 18):
        print("You may enter the private club")
    else:
        print("You may enter the playground")
else:
    if (age >= 18):
        print("You need a membership before entering the club")
    else:
        print("You need membership to access the playground")