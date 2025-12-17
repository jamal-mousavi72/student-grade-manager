import json

# گرفتن نام برای جستجو
search_name = input("Enter student name: ")
with open("student.json", "r") as s:
    students = json.load(s)
print(students)
