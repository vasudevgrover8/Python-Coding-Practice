num = int(input("Enter a number: "))
for row in range(1, num + 1):
    for col in range(1, num - row + 2):
        print(col, end = " ")
    print()