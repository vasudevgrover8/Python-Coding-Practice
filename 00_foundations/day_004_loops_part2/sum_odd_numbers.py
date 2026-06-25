num = int(input("Enter a number: "))
sum_of_odd = 0
for i in range(1, num + 1):
    if i % 2 != 0:
        sum_of_odd = sum_of_odd + i
print(sum_of_odd)