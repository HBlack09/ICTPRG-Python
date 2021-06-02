import math

values = [2.3, 7.9, -3.4, 4.2]
minNum = 0

for i in values:
    minNum = i if i < minNum else minNum

print(f"Minimum Number: {minNum}")
