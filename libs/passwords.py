try:
    # archivo .txt para almacenar las contraseñas
    with open("txt/passwords.txt", "r") as f:
        passwords = f.read()

    # ver contraseñas
    def view_pass():
        # datos actualizados
        with open("txt/passwords.txt", "r") as f:
            return f.read()

    # agregar contraseñas
    def add_pass(service, username, password):
        with open("txt/passwords.txt", "a") as f:
            f.write(f"{service} | {username} | {password}\n")

    # actualizar contraseñas
    def update_pass(pass_id, service, username, password):
        # releer el archivo
        with open("txt/passwords.txt", "r") as f:
            lines = f.read().splitlines()

        if 0 <= pass_id < len(lines):
            lines[pass_id] = f"{service} | {username} | {password}"
            with open("txt/passwords.txt", "w") as f:
                f.write("\n".join(lines) + "\n")
        else:
            print("Password not found.")

    # eliminar contraseñas
    def delete_pass(pass_id):
        # releer el archivo
        with open("txt/passwords.txt", "r") as f:
            lines = f.read().splitlines()

        if 0 <= pass_id < len(lines):
            del lines[pass_id]
            with open("txt/passwords.txt", "w") as f:
                if lines:
                    f.write("\n".join(lines) + "\n")
        else:
            print("Password not found.")

except FileNotFoundError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
    print("Run app.py please")