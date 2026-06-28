n = int(input("Enter the count of numbers: "))
positive_count = 0
negative_count = 0
zero_count = 0
print("Enter the numbers: ")
for i in range(1, n + 1):
    num = int(input())
    if num > 0:
        positive_count = positive_count + 1
    elif num == 0:
        zero_count = zero_count + 1
    else:
        negative_count = negative_count + 1
print("Positive: ", positive_count, "\nZero: ", zero_count, "\nNegative: ", negative_count)