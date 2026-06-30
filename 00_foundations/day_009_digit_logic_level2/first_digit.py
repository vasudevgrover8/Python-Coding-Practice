num = int(input("Enter a number: "))

while num >= 10:
    digits = num % 10
    num = num // 10

print(num)