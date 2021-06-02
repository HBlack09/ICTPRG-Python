import math

#create and open the output file
f = open("Factorials.txt", "a")

#Define a range and find the factorial
for i in range (1,11):
   f.write(f"{math.factorial(i)}\n")

#Close the output file
f.close()
