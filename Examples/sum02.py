import math
# sum example
numbers = [2,3,5,8,2,5.2,10.5,12,15.9,1]
total=0.0
i=0
num_min = numbers[0]
while i < len(numbers):
    total += numbers[i]
    # Updating the minimum
    if (numbers[i]<num_min):
        num_min = numbers[i]
    i += 1
print("minimum: ", num_min)
print("total: ",total)
avg = total / (len(numbers))
print("average: ", avg)
print( sum(numbers))