first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
contact_number = input("Enter contact number: ")
course = input("Enter your course: ")

student_info = f"Last Name: {last_name}\nFirst Name: {first_name}\nAge: {age}\nContact Number: {contact_number}"
with open ("Students.txt", "a") as file:
    file.write(student_info)
    print("\nStudent information has been saved to 'student.txt'.")
    