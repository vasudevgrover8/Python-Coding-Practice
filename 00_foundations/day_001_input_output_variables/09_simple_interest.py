# Input: Principal amount, interest rate, and time period
# Process: Use the simple interest formula
# Output: Simple interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period: "))

simple_interest = (principal * rate * time) / 100
print("Simple interest:", simple_interest)
