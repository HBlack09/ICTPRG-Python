# Search for a target string.
# Have the user input something to search for.
# Put this into a while loop with 'x' to end the search
#      0      1        2
arr = ["hat", "watch", "baseball", "car", "pen", "disk", "glasses"]
print("Searching the list: ", arr)
targ=""
while (True):
    targ = input("Enter item to search or 'x' to finish: ")
    if targ == "x":
        break
    print("Searching for " + targ)
    found = False
    i=0
    while (i<len(arr)):
        # print("arr[i]:",arr[i])
        if targ.lower() == arr[i]:
            found = True
            print("found " + arr[i])
        i = i+1
    if found == False:
        print("not found")
    


