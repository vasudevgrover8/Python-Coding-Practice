# DEBUG THE CODE BELOW FOR GETTING TRIANGLE STAR PATTERN

# n = int(input("Enter a number: "))

# for row in range(1, n + 1):
#     for col in range(1, n + 1):
#         print("*", end=" ")
#     print()

n = int(input("Enter a number: "))
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print("*", end = "")
    print()