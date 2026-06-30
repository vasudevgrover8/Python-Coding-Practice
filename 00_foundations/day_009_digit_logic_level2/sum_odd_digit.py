num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digits = num % 10
    
    if digits % 2 != 0:
        sum = sum + digits
    
    num = num // 10

print(sum)