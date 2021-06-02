# Sum maxNum numbers.
maxNum = 4
sum = 0
for count in range(maxNum):
    #num = int( input("Enter an integer: "))
    num = float( input("Enter a number: "))
    # sum = sum + num
    sum += num
print("The sum is: " + str(sum))
