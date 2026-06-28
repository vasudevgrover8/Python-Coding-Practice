n = int(input("Enter the count of numbers: "))
max_num = 0
print("Enter the numbers: ")
for i in range(1, n + 1):
    num = int(input())
    if i == 1:
        max_num = num
    else:
        if num > max_num:
            max_num = num
        
print(max_num)