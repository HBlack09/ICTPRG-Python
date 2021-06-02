def FibonacciAdder(x):
    num1 = 0
    num2 = 1
    count = 0
    total = 0
    
    while count < x:
        current = num1 + num2
        total += num1
        num1 = num2
        num2 = current
        count += 1
        
    return total

print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))
