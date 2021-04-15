#Ask user to input date
date = input("Enter a date in the format dd/mm/yyyy: ")

#Split date into lists
dateList = date.split("/")

#Printing the date 
print(f"Date: {dateList[0]}")
print(f"Date: {dateList[1]}")
print(f"Date: {dateList[2]}")