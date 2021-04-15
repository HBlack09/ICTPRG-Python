#Tell the system what the correct username & password are
correctuser = "bob"
correctpass = "password1234"

#Request username & password from the user to compare against the list of allowed variables
username = input("Enter Username: ")
password = input("Enter Password: ")

#check if the given username & password match the list of correct usernames and passwords
if username == correctuser and password ==correctpass:
    print("Access Granted!")
else:
    print("Access Denied! Contact System Administrator")