import csv

filename = "student.csv"

def add(name, rollNo, marks):
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, rollNo, marks])
        print(f"\nStudent '{name}' added successfully!\n")

def search(rollNo):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if row and row[1] == rollNo:
                print("\nStudent found")
                print(f"Name: {row[0]}, Roll no: {row[1]}, Marks: {row[2]}")
                found = True
                break
        if not found:
            print("\nStudent not found")

def students():
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        student_list = list(reader)
        if student_list:
            print("\nStudents List")
            for i, row in enumerate(student_list, 1):
                print(f"{i}. Name: {row[0]}, Roll No: {row[1]}, Marks: {row[2]}")
        else:
            print("\nNo students found")

def update(rollNo, new_marks):
    students = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        students = list(reader)

    updated = False
    for row in students:
        if row and row[1] == rollNo:
            row[2] = new_marks
            updated = True

    if updated:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(students)
        print("\nMarks updated successfully!")
    else:
        print(f"\nStudent with roll no {rollNo} not found")

def delete(rollNo):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        students = [row for row in reader if row and row[1] != rollNo]

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print("\nStudent deleted successfully!")

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Search Student")
    print("3. View All Students")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        marks = input("Enter marks: ")
        add(name, roll_no, marks)

    elif choice == "2":
        roll_no = input("Enter roll number to search: ")
        search(roll_no)

    elif choice == "3":
        students()

    elif choice == "4":
        roll_no = input("Enter roll number to update: ")
        new_marks = input("Enter new marks: ")
        update(roll_no, new_marks)

    elif choice == "5":
        roll_no = input("Enter roll number to delete: ")
        delete(roll_no)

    elif choice == "6":
        print("\nExiting...!")
        break

    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")
