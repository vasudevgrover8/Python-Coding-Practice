num = int(input("Enter a number: "))

original_num = num
num_squared = num ** 2
count_digits_of_num = 0

temp = num

if temp == 0:
    count_digits_of_num = 1
else:
    while temp > 0:
        temp = temp // 10
        count_digits_of_num = count_digits_of_num + 1

divisor = 10 ** count_digits_of_num
last_digits = num_squared % divisor

if last_digits == original_num:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")