# Input: Marks of 5 subjects
# Process: Add the marks and calculate the percentage
# Output: Total marks and percentage

subject_1 = float(input("Enter the marks of subject 1: "))
subject_2 = float(input("Enter the marks of subject 2: "))
subject_3 = float(input("Enter the marks of subject 3: "))
subject_4 = float(input("Enter the marks of subject 4: "))
subject_5 = float(input("Enter the marks of subject 5: "))

total_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
percentage = (total_marks / 500) * 100

print("Total marks:", total_marks)
print("Percentage:", percentage)
