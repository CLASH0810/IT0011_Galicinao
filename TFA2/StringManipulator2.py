first_name = input ("Enter your first name: ")
last_name = input ("Enter your last name: ")
full_name = first_name + " " + last_name

upper_case_name = full_name.upper()
lower_case_name = full_name.lower()

name_length = len(full_name)

print("Full Name:" , full_name)
print("Full Name (Upper case)", upper_case_name)
print("Full name (Lower case)", lower_case_name)
print("Length of Full Name,", name_length)