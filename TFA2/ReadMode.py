print("Reading Student Information.\n")
try:
    with open("Students.txt" , "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: 'Students.txt' file not found. Please save student data first.")