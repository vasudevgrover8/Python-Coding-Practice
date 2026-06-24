num = int(input("Enter a number: "))
count = 0
while num >= 1:
    num = num // 10
    count = count + 1
    print(num, count)
print(count)