num = int(input("Enter a number: "))
num_alias = num
reverse = 0

if num < 0:
    print("No palindrome")

else:    
    while num >= 1:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if reverse == num_alias:
        print("Palindrome")  
    else:
        print("Not a palindrome")