numbers = [0,1,2,3,4,5]
numbers[2] = 90
# [0, 1, 90, 3, 4, 5]
print(numbers)
print()
#lst = [10] * 5
#print(lst)
s = sum(numbers)
print("sum: ",s)
n = len(numbers)
print("length: ", n)
# Convert int to float (decimal) type
avg = float(s)/n
print(avg)
print()
#
def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num += t           
    avg = sum_num / len(num)
    return avg

print(cal_average(numbers) )
print(cal_average([1,2,3]))
print(cal_average([1,2,3,4,5,6,7]))