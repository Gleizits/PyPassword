import libs.db as db
import libs.encryption as enc
import os


def main():
    print("Starting the application...")
    os.system("clear")
    print(
        """
        Welcome to PyPassword Cli developed in Python!
                😀😀😀😀😀😀😀😀😀
        This CLI was developed by Gleizits. The source code can be found on my GitHub. Thank you for downloading it.
        Loading Passwords...
          """
    )
    a = input("Press Enter to continue...")
    if a == "":
        os.system("clear")

        while True:
            print(
                """
            TODO List Menu:
            1. Add Password
            2. View Passwords
            3. Update Password
            4. Delete Password
            5. Exit
            """
            )
            choice = int(input("Choose an option (1-5): "))

            if choice == 1:
                title = input("Enter your password: ")
                description = input("Enter the service password: ")
                status = input("Enter the username of the password owner: ")
                add_passw(id, password_encrypted, username)
            elif choice == 2:
                view_passw()
            elif choice == 3:
                task_id = int(input("Enter task ID to update: "))
                title = input("Enter new task title: ")
                description = input("Enter new task description: ")
                status = input("Enter new task status (pending/completed): ")
                update_passw(task_id, title, description, status)
            elif choice == 4:
                task_id = int(input("Enter task ID to delete: "))
                delete_passw(task_id)
            elif choice == 5:
                print("Exiting the application..... \n Goodbye!😀")
                break
            else:
                print("Invalid choice. Please try again.")

            input("Press Enter to continue...")
            os.system("cls")


if __name__ == "__main__":
    main()
