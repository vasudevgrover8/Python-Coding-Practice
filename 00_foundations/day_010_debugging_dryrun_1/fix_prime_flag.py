# Goal: Check whether number is prime using flag

num = int(input("Enter a number: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
    else:
        is_prime = True

if is_prime == True:
    print("Prime")
else:
    print("Not Prime")
    
# FIXED CODE
'''
num = int(input("Enter a number: "))

is_prime = True

if num == 0 or num == 1:
    print("Not Prime")

else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False

    if is_prime == True:
        print("Prime")
    else:
        print("Not Prime")
'''