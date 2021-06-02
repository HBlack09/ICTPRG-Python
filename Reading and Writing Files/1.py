#Request Input
x1 = int(input("Please write down any positive number: "))
y1 = int(input("Write down another number: "))

#Create output file
f = open("math.txt", "a")

#Print output to file
f.write(f"{x1 + y1}")

#Close file
f.close()

