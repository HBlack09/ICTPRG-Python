list1 = []
print("Enter item or x to terminate: ")
item = input("Enter item: ")
while item != "x":
    list1.append(item)
    print("Enter item or x to terminate: ")
    item = input("Enter item: ")
print("Shopping list: ", list1)
