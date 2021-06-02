import re
symbols = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

def GetPassword(password):
    noPass = True if "password" not in password.lower() else False
    lenPass = True if len(password) > 6 else False
    contUpper = True if any(i.isupper() for i in password) else False
    contLower = True if any(i.islower() for i in password) else False
    contSymbol = True if symbols.search(password) != None else False
    contNumber = True if re.findall(r'\d', password) else False

    if noPass and lenPass and contUpper and contLower and contSymbol and contNumber:
        return True
    else:
        return False

while True:
    password = input("Enter a password: ")
    if GetPassword(password) == True:
        if password == input("Please verify your password: "):
            print("Valid Password!")
            break
        else:
            print("Your password did not match, please try again...")
    else:
        print("Invalid Password, please try again...")
