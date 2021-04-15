#Ask user their year of birth
birthyear = int(input("What year were you born?"))

#Convert birthyear to age
age = 2021 - birthyear

#State their age
print(f"You are {age} years old.")

#If age is under 18, print leave message
if age < 18:
    print("Get lost you child")

#Otherwise, welcome them
else:
    print("Welcome to my humble bar")