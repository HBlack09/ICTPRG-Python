desc = ["tasty", "big", "nutritious"]
fruit = ["apple", "bannana", "orange", "nashi pair"]

# nested loop
for x in desc:
    for y in fruit:
        print(x,y)

print()
for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            print(""+str(x)+str(y)+str(z))