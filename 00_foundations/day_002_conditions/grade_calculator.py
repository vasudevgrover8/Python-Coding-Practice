#Input: Marks
#Process: Assign the grade to a range of marks using if-elif-else
#Output: Grade 

marks = int(input("Enter your marks: "))
if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F") 