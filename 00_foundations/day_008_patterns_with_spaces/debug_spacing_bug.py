''' # Input: One number n
    # Process: Print centered pyramid
    # Output: Centered star pyramid
    
    n = int(input("Enter a number: "))

    for row in range(1, n + 1):
        spaces = n - row
        stars = 2 * row - 1

        for space in range(spaces):
            print(" ", end="")

        for star in range(stars):
            print("*", end=" ")

        print()'''

n = int(input("Enter a number: "))

for row in range(1, n + 1):
    spaces = n - row
    stars = 2 * row - 1

    for space in range(spaces):
        print(" ", end = " ")

    for star in range(stars):
        print("*", end = " ")

    print()