num  = int(input("Enter a number: "))
factors_sum = 0
for i in range(1, num):
    if num % i == 0:
        factors_sum = factors_sum + i 
if factors_sum == num:
    print("Perfect number")
else: 
    print("Not a perfect number")