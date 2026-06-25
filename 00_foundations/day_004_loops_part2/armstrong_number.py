num = int(input("Enter a number: "))
num_alias = num
cube = 0
while num >= 1:
    digit = num % 10
    num = num // 10
    cube = cube + (digit ** 3)

if cube == num_alias:
    print("Armstrong number")
else:
    print("Not an Armstrong number")