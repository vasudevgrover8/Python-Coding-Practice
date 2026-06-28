n = int(input("Enter the count of numbers: "))
sum = 0
print("Enter the numbers")
for i in range(1, n + 1):
    num = int(input())
    if num % 2 == 0 or num % 7 == 0:
        sum = sum + num
print(sum)