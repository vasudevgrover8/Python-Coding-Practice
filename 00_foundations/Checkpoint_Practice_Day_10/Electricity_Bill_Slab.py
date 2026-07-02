units = int(input("Enter the units consumed: "))
bill = 0

if units <= 100:
    bill = bill + (units) * 5
    print(bill)
elif units <= 300:
    bill = bill + 500 + (units - 100) * 70
    print(bill)
else:
    bill = bill + 500 + 1400 + (units - 300) * 10
    print(bill)

print(bill)
    