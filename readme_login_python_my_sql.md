# 🔐 Login System with Python & MySQL

Sistema de autenticación **real** construido desde cero usando **Python**, **MySQL** y **bcrypt**. Incluye registro de usuarios, login seguro con hash de contraseñas y conexión directa a base de datos.

Este proyecto nace como práctica de backend **nivel trabajo real**: instalación de MySQL, conexión, debugging de errores comunes en Windows y manejo correcto de tipos (`str` vs `bytes`).

---

## 🚀 Features

- ✅ Registro de usuarios
- ✅ Login con validación segura
- ✅ Contraseñas hasheadas con `bcrypt`
- ✅ Base de datos MySQL
- ✅ Manejo de errores comunes
- ✅ Estructura limpia de proyecto

---

## 🧱 Tech Stack

- **Python** (3.11 / 3.12 recomendado)
- **MySQL Server**
- **mysql-connector-python**
- **bcrypt**

---

## 📂 Project Structure

```
login_connecting_to_mysql/
│
├── main.py        # Entry point (CLI)
├── auth.py        # Register & login logic
├── db.py          # MySQL connection
├── README.md
```

---

## ⚙️ Requirements

### Python
> ⚠️ **IMPORTANTE:** No usar Python 3.14 (incompatible con mysql-connector).

Recomendado:
```bash
Python 3.11 o 3.12
```

### MySQL
- MySQL Server corriendo como servicio (`MySQL80`)
- Usuario `root` configurado

---

## 📦 Installation

### 1️⃣ Instalar dependencias

```bash
pip install mysql-connector-python bcrypt
```

---

### 2️⃣ Crear base de datos

En MySQL:

```sql
CREATE DATABASE auth_system;
USE auth_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔌 Database Connection (`db.py`)

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="auth_system"
    )
```

---

## 🔐 Authentication Logic (`auth.py`)

- Contraseñas **NO** se guardan en texto plano
- Se usa `bcrypt` para hash y verificación

Manejo explícito de tipos (`bytes` vs `str`) para compatibilidad con MySQL.

---

## ▶️ Run the Project

Desde la carpeta del proyecto:

```bash
python main.py
```

Menú:
```
1. Register
2. Login
q. Exit
```

---

## 🧪 Example

```
User: noxvane
Password: root
✅ Login exitoso
```

```
User: elisson
Password: admin
❌ Usuario no existe
```

---

## 🧠 What This Project Demonstrates

- Backend fundamentals
- MySQL integration
- Secure authentication
- Debugging real-world errors
- CLI-based user flow

---

## 📌 Next Improvements

- 🔑 JWT Authentication
- 🌐 Flask / FastAPI API
- 🔒 Environment variables
- 🎨 Frontend integration

---

## 👤 Author

**Elisson (NoxVane)**  
Backend & Python Developer in progress 🚀

---

## 📜 License

MIT License

