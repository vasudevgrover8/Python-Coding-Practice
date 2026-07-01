# Goal: Print right triangle star pattern

n = int(input("Enter a number: "))

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print("*")
    print()
    
# FIXED CODE
'''
n = int(input("Enter a number: "))

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print("*", end = " ")
    print()
'''