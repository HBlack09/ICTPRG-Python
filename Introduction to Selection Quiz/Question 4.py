#Ask user to input to input username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

#Define what the correct username and password are + grant/deny access
if username == "bob" and password == "password1234":
         print("Access Granted!")
elif username == "fred" and password == "happyPass122": 
    print("Access Granted!")
elif username == "lock" and password == "passwithlock44": 
     print("Access Granted!")
else: 
     print("Access Denied!")
