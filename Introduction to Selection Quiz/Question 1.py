#Ask the user for their name and save as variable name
name = input("What is your name?")

#Check if their name is frank or george
if name == "frank" or name == "george":

    #say hello
    print("Hello" + " " + name)

#if their name is not frank or george
else:

        #Say no
        print("Sorry, you cannot access the system")