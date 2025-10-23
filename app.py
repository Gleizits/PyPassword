import libs.passwords as passwords
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
                password = input("Enter your password: ")
                service = input("Enter the service name: ")
                username = input("Enter the username of the password owner: ")
                enc.add_pass(service, username, enc.password)
            elif choice == 2:
                view_pass()
            elif choice == 3:
                task_id = int(input("Enter password ID to update: "))
                password = input("Enter new password: ")
                service = input("Enter new password service: ")
                username = input("Enter new username: ")
                update_pass(task_id, enc.password, service, username)
            elif choice == 4:
                task_id = int(input("Enter password ID to delete: "))
                delete_pass(task_id)
            elif choice == 5:
                print("Exiting the application..... \n Goodbye!😀")
                break
            else:
                print("Invalid choice. Please try again.")

            input("Press Enter to continue...")
            os.system("cls")


if __name__ == "__main__":
    main()
