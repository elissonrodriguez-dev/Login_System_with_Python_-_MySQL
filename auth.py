import bcrypt
from db import get_connection

def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
        (username, password_hash)
    )
    
    conn.commit()
    cursor.close()
    conn.close
    print("User registred")
    
def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password_hash FROM users WHERE username = %s",
        (username,)
    )

    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if not result:
        print("❌ Usuario no existe")
        return

    stored_hash = result[0]

    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode()

    if bcrypt.checkpw(password.encode(), stored_hash):
        print("✅ Login exitoso")
    else:
        print("❌ Contraseña incorrecta")

    