print("Find maximum of v")
v = [2, -5, 12, 3]
print("v: ",v)

maximum = max(v)
#print("maximum: ", maximum)

val2 = v[0]
for k in v:
    if val2 < k:
        val2 = k
#print("val2: ", val2)
print("lenght of v: ", len(v))
print()
val=v[0]
i=1
while (i<len(v)):
    #print("i: ",i)
    #print("v[i]: ",v[i])
    #print("val: ",val)
    if val < v[i]:
        val = v[i]
    i = i+1
#print("Exited loop")
#print("i: ", i)
print("Max of v: ", val)