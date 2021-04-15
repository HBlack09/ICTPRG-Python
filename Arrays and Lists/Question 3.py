#Import math.py
import math

#List the values, subtotal, mean and maximum number
values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
subTotal = 0
mean = 0
maxNum = 0

#Define what you want it to do
for i in values:
    subTotal = subTotal + i
    mean = math.floor(subTotal / len(values))
    maxNum = i if i > maxNum else maxNum

#Print the numbers
print(f"Sub Total: {subTotal}")
print(f"Average: {mean}")
print(f"Maximum Number: {maxNum}")