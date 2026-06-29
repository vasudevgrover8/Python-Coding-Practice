num = int(input("Enter a number: "))
for row in range(1, num + 1):
    for spaces in range(1, num - row + 1):
        print(" ", end = " ")
    for stars in range(1, row + 1):
        print("*", end = " ")
    print()