num = int(input("Enter a number: "))
count_4 = 0
count_6 = 0
count_4_and_6 = 0
count_4_or_6 = 0
for i in range(1, num + 1):
    if i % 4 == 0 and i % 6 == 0:
        count_4_and_6 = count_4_and_6 + 1 
    if i % 4 == 0 or i % 6 == 0:
        count_4_or_6 = count_4_or_6 + 1
    if i % 6 == 0:
        count_6 = count_6 + 1
    if i % 4 == 0:
        count_4 = count_4 + 1

print("Divisible by 4: ", count_4)
print("Divisible by 6: ", count_6)
print("Divisible by 4 or 6: ", count_4_or_6)
print("Divisible by 4 and 6: ", count_4_and_6)