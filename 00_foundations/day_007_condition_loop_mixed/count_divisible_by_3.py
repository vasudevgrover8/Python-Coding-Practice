n = int(input("Enter the count of numbers"))
print("Enter the numbers that you want to check")
count = 0
for i in range(1, n + 1):
    num = int(input("Enter a number: "))
    if num % 3 == 0:
        count = count + 1
print(count)