#student Details 
print("Provide the student Details Below")
student_name = input("Student Name : ")
student_roll_number = input(" Student Roll Number : ")
student_branch = input("Which Branch does Student Belong : ")
student_age = input("Student Age : ")
student_sem = input("Student Semister : ")
student_section = input("Student Section : ")
student_college = input("Which College does Student Belong : ")
student_city = input("Student City : ")

#student Marks
print("Student Marks Details")
english = int(input("Enter your english marks : "))
mathematics = int(input("Enter your mathematics marks : "))
physics = int(input("Enter your physics marks : "))
chemistry = int(input("Enter your chemistry marks : "))
biology = int(input("Enter your biology marks : "))

#calculation
subjects = 5
max_marks = subjects*100
total_marks = english + mathematics + physics + chemistry + biology
avg_marks = total_marks/subjects
percentage = (total_marks / max_marks) *100
highest = max(english, mathematics, physics, chemistry, biology)
lowest = min(english, mathematics, physics, chemistry, biology)

#print, f-string
print("="*35)
print("Student report")
print("="*35)
print("--- Student Information ---")
print(f"Name : {student_name}\nRoll Nnumber :{student_roll_number}\nBranch :{student_branch}\nAge :{student_age}\nSemister :{student_sem}\nSection :{student_section}\nCollege :{student_college}\nCity :{student_city}")
print("---- Result ----")
print(f"Highest Marks : {highest}\nLowest Marks : {lowest}")
print(f"Total Marks : {total_marks}\nAverage Marks : {avg_marks:.2f}\npercentage : {percentage:.2f}%")

print("="*35)
