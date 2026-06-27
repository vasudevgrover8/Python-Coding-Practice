num = int(input("Enter a number: "))
prime_flag = False
if num == 2:
    print("Prime")
else:
    for i in range(2, num):
        if num % i  == 0:
            prime_flag = False
            break
        else:
            prime_flag = True
    if prime_flag == True:
        print("Prime")
    else:
        print("Not Prime")
        