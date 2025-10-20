import sqlite3 as sql
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "PY_PASS.db")

conn = None

try:
    # crear db y tabla si no existen
    os.makedirs(os.path.join(BASE_DIR, "db"), exist_ok=True)
    with sql.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT,
                password_encrypted TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )
        conn.commit()

    # Reabrir conexión para operaciones
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    conn.commit()

    # registrar contraseñas
    def register_pass(service, username, password_encrypted):
        cursor.execute(
            "INSERT INTO passwords (service, username, password_encrypted) VALUES (?, ?, ?)",
            (service, username, password_encrypted),
        )
        conn.commit()

    # ver contraseñas
    def view_passw():
        cursor.execute("SELECT id, service, username, created_at FROM passwords")
        return cursor.fetchall()

    # actualizar contraseñas
    def update_passw(pass_id, new_password_encrypted):
        cursor.execute(
            "UPDATE passwords SET password_encrypted = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (new_password_encrypted, pass_id),
        )
        conn.commit()

    # eliminar contraseñas, segun el id
    def delete_passw(pass_id):
        cursor.execute("DELETE FROM passwords WHERE id = ?", (pass_id,))
        conn.commit()

except sql.Error as e:
    print(f"Oh nooo error!!!: {e}")

# ejecuta app.py, no este archivo
if __name__ == "__main__":
    if conn:
        conn.close()
        print("Open main.py please.")
