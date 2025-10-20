from cryptography.fernet import Fernet
import os

# ruta de las contraseñas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(BASE_DIR, "secret.key")

# generar cifrado
def generate_key():
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as key_file:
            key_file.write(key)
    else:
        return 0

# cargar cifrado
def load_key():
    if not os.path.exists(KEY_PATH):
        raise FileNotFoundError("secret.key no exist")
    with open(KEY_PATH, "rb") as key_file:
        return key_file.read()

# encriptando contraseñas
def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted.decode()

# desencriptando contraseñas
def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password.encode())
    return decrypted.decode()


if __name__ == "__main__":
    print("Please run app.py")
