from libs.passwords import add_pass, view_pass, update_pass, delete_pass
import os


def main():
    print("Starting the application...")
    os.system("clear")
    print(
        """
        Welcome to PyPassword Cli developed in Python!
                😀😀😀😀😀😀😀😀😀
        This CLI was developed by Gleizits. The source code can be found on my GitHub. Thank you for downloading it.
        Loading...
          """
    )
    a = input("Press Enter to continue...")
    if a == "":
        os.system("clear")

        while True:
            print(
                """
                Password Manager Menu:
                1. Add Password
                2. View Passwords
                3. Update Password
                4. Delete Password
                5. Exit
                """
            )

            choice = int(input("Choose an option (1-5): "))

            if choice == 1:
                service = input("Enter the service name: ")
                username = input("Enter the username of the password owner: ")
                password = input("Enter your password: ")
                add_pass(service, username, password)
            elif choice == 2:
                passwords = view_pass()
                print("\n--- Stored Passwords ---")
                print(passwords)
            elif choice == 3:
                passwords = view_pass()
                print("\n--- Current Passwords ---")
                print(passwords)
                pass_id = int(input("\nEnter password ID to update: "))
                service = input("Enter new service name: ")
                username = input("Enter new username: ")
                password = input("Enter new password: ")
                update_pass(pass_id, service, username, password)
            elif choice == 4:
                passwords = view_pass()
                print("\n--- Current Passwords ---")
                print(passwords)
                pass_id = int(input("\nEnter password ID to delete: "))
                delete_pass(pass_id)
            elif choice == 5:
                print("Exiting the application..... \n Goodbye!😀")
                break
            else:
                print("Invalid choice. Please try again.")

            input("Press Enter to continue...")
            os.system("cls")


if __name__ == "__main__":
    main()
