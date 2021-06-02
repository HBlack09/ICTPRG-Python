def GetEmailAddress(email):
    if "@" in email:
        accountName = email.split("@")[0]
        domainName = email.split("@")[1]

        if (len(accountName) > 2 and len(accountName) <= 32) and (len(domainName) > 2 and len(domainName) <=32) and ("." in domainName):
            return True
    return False

while True:
    email = input("Enter an email address: ")
    if GetEmailAddress(email): 
        print(email)
        break
    else:
        print("Not a valid email, please try again...")
