num = int(input("Enter a number: "))
count = 0
while num > 0:
    digits = num % 10
    if digits % 2 == 0:
        count = count + 1
    num = num // 10
    
print(count)