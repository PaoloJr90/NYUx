number_of_students = int(input("Please enter the number of students in the class:"))

print("Please enter the students' grade (in separate lines):")
grades_sum = 0
for i in range(number_of_students):
    curr_grade = int(input())
    grades_sum += curr_grade

average = grades_sum / number_of_students
print("The class average =", average)