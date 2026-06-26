num = int(input("Enter a number: "))
for row in range(1, num + 1):
    spaces = num - row
    stars = 2*row - 1
    for spaces in range(spaces):
        print(" ", end = " ")
    for stars in range(stars):
        print("*", end = " ")
    print()