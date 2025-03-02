import csv
import os

# Define the file name for saving records
filename = "students_records.csv"

# List to store student records
data = []

# Function to load data from a file
def open_file():
    global data
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            data = [tuple(row) for row in reader]
        print("File loaded successfully!")
    else:
        print("File not found!")

# Function to save data to a file
def save_file():
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("File saved successfully!")

# Function to save as a new file
def save_as_file(new_filename):
    with open(new_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"File saved as {new_filename} successfully!")

# Function to display all student records
def show_all():
    for record in data:
        print(record)

# Function to order by last name
def order_by_lastname():
    sorted_data = sorted(data, key=lambda x: x[1].split()[-1])
    for record in sorted_data:
        print(record)

# Function to order by grade
def order_by_grade():
    sorted_data = sorted(data, key=lambda x: (0.6 * float(x[2]) + 0.4 * float(x[3])), reverse=True)
    for record in sorted_data:
        print(record)

# Function to show a specific student record
def show_student_record(student_id):
    for record in data:
        if record[0] == student_id:
            print(record)
            return
    print("Student not found!")

# Function to add a new record
def add_record():
    student_id = input("Enter Student ID (6-digit number): ")
    name = input("Enter Student Name (First Last): ")
    class_standing = input("Enter Class Standing Grade: ")
    major_exam = input("Enter Major Exam Grade: ")
    
    data.append((student_id, name, class_standing, major_exam))
    print("Record added successfully!")

# Function to edit a record
def edit_record(student_id):
    for i, record in enumerate(data):
        if record[0] == student_id:
            name = input("Enter new Student Name (First Last): ")
            class_standing = input("Enter new Class Standing Grade: ")
            major_exam = input("Enter new Major Exam Grade: ")
            data[i] = (student_id, name, class_standing, major_exam)
            print("Record updated successfully!")
            return
    print("Student not found!")

# Function to delete a record
def delete_record(student_id):
    global data
    data = [record for record in data if record[0] != student_id]
    print("Record deleted successfully!")

# Menu system
def menu():
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            open_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            new_filename = input("Enter new filename: ")
            save_as_file(new_filename)
        elif choice == "4":
            show_all()
        elif choice == "5":
            order_by_lastname()
        elif choice == "6":
            order_by_grade()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            show_student_record(student_id)
        elif choice == "8":
            add_record()
        elif choice == "9":
            student_id = input("Enter Student ID to edit: ")
            edit_record(student_id)
        elif choice == "10":
            student_id = input("Enter Student ID to delete: ")
            delete_record(student_id)
        elif choice == "11":
            break
        else:
            print("Invalid choice! Please try again.")

# Run the menu system
menu()
