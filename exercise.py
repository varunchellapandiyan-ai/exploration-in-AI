name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))
total = 0

for i in range(1, n + 1):
    mark = float(input(f"Enter mark for subject {i}: "))
    total += mark

percentage = total / n

if percentage >= 90:
    performance = "Outstanding"
    grade = "A+"
elif percentage >= 80:
    performance = "Excellent"
    grade = "A"
elif percentage >= 70:
    performance = "Very Good"
    grade = "B"
elif percentage >= 60:
    performance = "Good"
    grade = "C"
elif percentage >= 50:
    performance = "Average"
    grade = "D"
else:
    performance = "Needs Improvement"
    grade = "F"

print("\n--- Academic Performance ---")
print("Student Name :", name)
print("Total Marks  :", total)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("Performance  :", performance)