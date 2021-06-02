a = [2.3, 7.9, -3.4, 4.2]
print("a: ",a)
print("len(a): ",len(a))
print("min(a): ", min(a) )

# Initialise the counter variable
i=1
# Current minimum
minval = a[0]
while i<len(a):
    print("minval: ", minval)
    if a[i] < minval:
        minval = a[i]
    i = i+1
print("final min val: ", minval)
