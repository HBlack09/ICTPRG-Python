#Define what the program is looking for
username = input("Username?: ")
password = input("Password?: ")

#Define the correct condition
Passuser = f"{username}:{password}"

#Read the file with the correct details
loginFile = open('loginFile.txt', 'r')

#Check the details against the correct ones listed
for i in loginFile:
    if Passuser == i.strip():
        print("Access Granted!")
        exit()

#Close the file
loginFile.close()

#If details are wrong:
print("Access Denied, contact system admin.")

