num = int(input("Enter a number: "))
digit = 0
reverse = 0
while num >= 1:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print(reverse)
    