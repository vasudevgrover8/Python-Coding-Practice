#Input: Year
#Process: Use the remainder operator 
#Output: Leap year or not

year = int(input("Enter the year: "))
if year % 400:
    print("Leap Year")
elif year % 100:
    print("No leap year")
elif year % 4:
    print("Leap year")
else:
    print("Not a leap year")