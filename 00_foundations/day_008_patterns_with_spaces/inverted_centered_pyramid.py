num = int(input("Enter a number: "))
for row in range(0, num):
    for spaces in range(0, row):
        print(" ", end = " ")
    for stars in range(0, 2 *num - 2 * row - 1):
        print("*", end = " ")
    print()