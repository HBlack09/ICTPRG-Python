#Ask user to input date
date = input("Enter a date in the format dd/mm/yyyy: ")

#Split date into lists
dateList = date.split("/")

#Printing the date 
print(f"Day: {dateList[0]}")
print(f"Month: {dateList[1]}")
print(f"Year: {dateList[2]}")
