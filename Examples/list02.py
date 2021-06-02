# List has dupicates
x4 = [2.5, 'a', 7, 'abc', 46, 7]
print(x4)
# remove deletes the first instance only
x4.remove(7)
print(x4)
x4.remove(7)
print(x4)
# This code fails because the element must
#  alread exist in the list.
#  x4.remove("def")
#
# Delete last element in the list
x4.pop(-1)
print(x4)
# Delete the first element in the list
x4.pop(0)
print(x4)