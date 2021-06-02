#val = 6
# Tess if val:  0 <= val <= 5
#if (val >= 0) and (val <=5):
#    print("in range")
#else:
#    print("out of range.")
    
# Made the test into a function
def valTest(val):
    print("testing value:",val)
    if(val >=0) and (val <=5):
        print("in range")
    else:
        print("out of range.")

valTest(-1)
valTest(0)
valTest(1)
valTest(6)
