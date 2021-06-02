#Request Names
Name = input("(Hit enter when list is complete) Names: ")
nameList = Name.split(" ")

#Create output file
f = open("people.txt", "a")

#Print output to file
for Name in nameList:
    f.write(Name + "\n")


#Close file
f.close()
