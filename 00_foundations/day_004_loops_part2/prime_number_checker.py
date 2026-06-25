num = int(input("Enter a number: "))
count = 0

if num <= 1:
    print("Not prime")

else:     
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
        
    if count > 2:
        print("Not prime")  
    else:
        print("prime")    
    
    
# Another version of the code:
# num = int(input("Enter a number: "))
# is_prime = False
# for i in range(2, (num//2) + 1):
#     if num % i == 0:
#         is_prime = False
# if(is_prime == True):
#     print("Prime")
# else:
#     print("Not Prime")