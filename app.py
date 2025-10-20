import libs.db as db
import os

if __name__ == "__main__":
    # ejemplo de uso de las funciones de la base de datos
    db.register_pass("MyPassword", "This is a test password", "active")