# String test
# Task: search the string for 'four'
s1 = 'one two three four five'
if 'four' in s1:
    print("Found " + "four" + " in " + s1)
else:
    print("Not found " + "four" + " in " + s1)

print()
s2="123"
# Is it a digit?
print(s2.isdigit())
# Is it alphanumeric?
print(s2.isalnum()) 
print(s2.isspace())
print()
#txt = "Abc"
#print("txt: ",txt)
#txt2 = txt.upper()
#print("txt2: ",txt2)
#txt3 = txt2.lower()
#print("txt3: ",txt3)

v1 = "Swan"
v2 = "sWan"
print( v1 == v2)
print( v1.lower() == v2.lower())
print( v1.upper() == v2.upper())
