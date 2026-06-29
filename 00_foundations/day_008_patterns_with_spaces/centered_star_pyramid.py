num = int(input("Enter a number: "))
for rows in range(1, num + 1):
    for spaces in range(1, num - rows + 1):
        print(" ", end = " ")
    for stars in range(1, 2 * rows):
        print("*", end = " ")
    print()