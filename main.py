import grade_calc
import json
import os  # برای چک کردن اینکه فایل وجود داره یا نه

try:
    # 1. گرفتن نام و نمرات
    name = input("Enter student name: ")
    grade_list = list(map(float, input("Enter grades: ").split()))

    average = grade_calc.calculate_average(grade_list)
    status = grade_calc.status_check(average)

    # دیکشنری اطلاعات دانشجو جدید
    new_student = {
        "name": name,
        "average": average,
        "status": status
    }

    # --- بخش جدید: خواندن دیتابیس قبلی ---

    # لیست کل دانشجوها
    all_students = []

    # چک میکنیم اگر فایل قبلا ساخته شده، بازش کنیم و اطلاعاتش رو بخونیم
    if os.path.exists("student.json"):
        with open("student.json", "r") as f:
            # دستور load فایل رو میخونه و تبدیل میکنه به لیست پایتون
            all_students = json.load(f)
            # نکته: اگر فایل قبلی فرمتش لیست نباشه (مثل تمرین قبلی)، ارور میده.
            # پس بهتره فایل student.json قبلی رو دستی پاک کنی تا از اول ساخته بشه.

    # --- اضافه کردن نفر جدید ---
    all_students.append(new_student)

    # --- ذخیره کردن کل لیست ---
    with open("student.json", "w") as f:
        json.dump(all_students, f)
        print(
            f"Student {name} added successfully! Total students: {len(all_students)}")

except ValueError:
    print("Error: Please enter numbers only.")
except Exception as e:
    print(f"Error: {e}")
