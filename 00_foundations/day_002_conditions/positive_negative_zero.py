#Input: Number
#Process: Compare the number with zero
#Output: Positive, Negative or Zero

number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")    
