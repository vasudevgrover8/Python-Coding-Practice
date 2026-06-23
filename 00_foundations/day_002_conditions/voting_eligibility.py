#Input: Age
#Process: Compare with 18
#Output: Eligibility

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")