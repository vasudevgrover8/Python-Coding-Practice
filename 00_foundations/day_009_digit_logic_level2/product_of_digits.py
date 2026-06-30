num = int(input("Enter a number: "))
product = 1
if num == 0:
    print(0)
else: 
    while num > 0:
        digits = num % 10
        num = num // 10
        product = product * digits
    print(product)