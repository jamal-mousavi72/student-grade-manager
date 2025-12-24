import json

# گرفتن نام برای جستجو
search_name = input("Enter student name: ")
with open("student.json", "r") as s:
    students = json.load(s)

for s in students:
    if s["name"].lower() == search_name.lower():

        print(
            f"Average is {s['average']} and Status is {s['status']}")
        break
else:
    print("Student not found!")
