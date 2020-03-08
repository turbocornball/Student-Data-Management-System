# Student Management System

import csv
# Define global variables
student_fields = ['ID_Number', 'Name', 'Year Level', 'Course']
student_database = 'students.csv'
 
 
def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")
 
 
def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    student_fields
    student_database
 
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)
 
    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
 
    print("Data saved successfully")
    input("Press any key to continue")
    return
 
 
def view_students():
    student_fields
    student_database
 
    print("--- Student Records ---")
 
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
 
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
 
    input("Press any key to continue")
 
 
def search_student():
    student_fields
    student_database
 
    print("--- Search Student ---")
    ID_Number = input("Enter ID No. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if ID_Number == row[0]:
                    print("----- Student Found -----")
                    print("ID_Number: ", row[0])
                    print("Name: ", row[1])
                    print("Year Level: ", row[2])
                    print("Course: ", row[3]
                    break
        else:
            print("ID No. not found in our database")
    input("Press any key to continue")
 
 
def update_student():
    student_fields
    student_database
 
    print("--- Update Student ---")
    ID_Number = input("Enter ID No. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID_Number == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1
 
    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("ID No. not found in our database")
 
    input("Press any key to continue")
 
 
def delete_student():
    student_fields
    student_database
 
    print("--- Delete Student ---")
    ID_Number = input("Enter ID No. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID_Number != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True
 
    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID No. ", ID_Number, "deleted successfully")
    else:
        print("ID No. not found in our database")
 
    input("Press any key to continue")
 
while True:
    display_menu()
 
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break
 
print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")