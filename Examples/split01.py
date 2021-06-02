# A string captures the user input. 
ans5 = "Fred 20"
print(ans5)
ans6 = ans5.split()
print(ans6)
# Extracting the information from the list.
nm = ans6[0]
print("name: ", nm)
# Extracting the age and converting it to an int
age = int(ans6[1])
print("age: ",age)
