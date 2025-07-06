stu_mark = {
    "Ram": 85,
    "Shyam": 92,
    "Mia": 78,
    "Steffy": 90,
    "Daniel": 88
}

name = input("Enter student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found!!")
