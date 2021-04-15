#Ask user for their mark
grade = int(input("What was your grade? "))

#Define what each mark is worth
if grade >= 90:
    print("Congrats! You got a \"High Dintinction\"")

elif grade < 90 and grade >= 80:
    print("You will recieve a \"Distinction\"")

elif grade < 80 and grade >= 70:
    print("You will recieve a \"Credit\"")

elif grade < 70 and grade >= 50:
    print("You will recieve a \"Pass\"")

else: 
    print("You failed.") 