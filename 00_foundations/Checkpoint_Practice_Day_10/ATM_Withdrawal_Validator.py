account_balance = int(input("Enter the balance of the account: "))
withdrawal_amount = int(input("Enter the withdrawal amount: "))

if withdrawal_amount <= 0 or withdrawal_amount % 100 != 0:
    print("Invalid withdrawal amount")
    
if withdrawal_amount > account_balance:
    print("Insufficient balance")

elif account_balance - withdrawal_amount < 500:
    print("Account balance cannot be below 500")

else:
    print("Withdrawal successful")
    print("Account balance: ", account_balance - withdrawal_amount)