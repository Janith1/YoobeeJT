from Database import create_user_table,  create_student_table
from User_Manager import add_user, view_users, search_user, delete_user, add_student, view_student

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. Add Student")
    print("3. View All Users & Students")
    print("4. Search User by Name")
    print("5. Delete User by ID")
    print("6. Exit")

def main():
    create_user_table()
    create_student_table()
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            add_user(name, email)
        elif choice == '2':
            stu_name = input("Enter student name: ")
            stu_email = input("Enter student email: ")
            add_student(stu_name, stu_email)
        elif choice == '3':
            #Display all users
            print("View All Users")
            users = view_users()
            for user in users:
                print(user)
            # Display all students
            print("View All Students")
            students = view_student()
            for student in students:
                print(student)
        elif choice == '4':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '5':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
