# Sum a loop of integers greater than zero.
sum = 0.0
#num = int(input("Enter a number or 0 to finish: "))
num = float(input("Enter a number or 0 to finish"))
while num != 0:
    sum += num
    #num = int(input("Enter a number of 0 to finish: "))
    num = float(input("Enter a number of 0 to finish: "))

print("sum: " + str(sum))
