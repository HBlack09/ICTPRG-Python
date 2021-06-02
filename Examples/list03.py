num1 = [1,2,3]
num2 = [100,200,300]
print("num2: ", num2)
# a += b   is the same as a = a + b
num2 += num1
print("num2: ", num2)
print()
# Appending to the end of the list
x = ['a']
print(x)
x += ['b']
print(x)
x += ['c']
print(x)
x.append('d')
print(x)
x.insert(1,'ab')
print(x)
# Type in and run
print()
#    -4  -3   -2   -1
#     0   1    2    3
x2 = ["a", "b","c","d"]
print(x2)
x2.insert(-3,"v")
print(x2)
# .pop(k) deletes the kth element
x2.pop(0)
print(x2)
# delete the last element
x2.pop(-1)
print(x2)