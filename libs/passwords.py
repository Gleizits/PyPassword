import os

# crear txt si no existe
if not os.path.exists("txt"):
    os.makedirs("txt")

# crear el archivo passwords.txt si no existe
if not os.path.exists("txt/passwords.txt"):
    with open("txt/passwords.txt", "w") as f:
        f.write("")

try:
    # ver contraseñas
    def view_pass():
        with open("txt/passwords.txt", "r") as f:
            content = f.read()
            if not content:
                return "No passwords"

            lines = content.splitlines()
            result = []
            for idx, line in enumerate(lines):
                result.append(f"[{idx}] {line}")
            return "\n".join(result)

    # agregar contraseñas a el archivo .txt
    def add_pass(service, username, password):
        with open("txt/passwords.txt", "a") as f:
            f.write(f"{service} | {username} | {password}\n")

    # actualizar contraseñas
    def update_pass(pass_id, service, username, password):
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
        with open("txt/passwords.txt", "r") as f:
            lines = f.read().splitlines()

        if 0 <= pass_id < len(lines):
            del lines[pass_id]
            with open("txt/passwords.txt", "w") as f:
                if lines:
                    f.write("\n".join(lines) + "\n")
        else:
            print("Password not found.")

except FileNotFoundError:
    print(f"Error: {e}")

if __name__ == "__main__":
    print("Run app.py please")
