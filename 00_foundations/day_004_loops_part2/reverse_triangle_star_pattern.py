num = int(input("Enter a number: "))
for row in range(0, num):
    for col in range(0, num - row):
        print("*", end = " ")
    print("")