import hashlib
import sqlite3
from flask import Flask, request

# Crear sitio web con Flask en el puerto 4850
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Crear base de datos SQLite y tabla para almacenar usuarios
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (nombre TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()

    # Función para almacenar usuarios y contraseñas en hash
    def almacenar_usuario(nombre, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute("INSERT INTO usuarios VALUES (?, ?)", (nombre, hashed_password))
        conn.commit()

    # Función para validar usuarios
    def validar_usuario(nombre, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute("SELECT COUNT(*) FROM usuarios WHERE nombre = ? AND password = ?", (nombre, hashed_password))
        result = c.fetchone()
        return result[0] > 0

    nombre = request.form['nombre']
    password = request.form['password']

    if validar_usuario(nombre, password):
        return 'Bienvenido, {}'.format(nombre)
    else:
        return 'Usuario o contraseña incorrectos'

if __name__ == '__main__':
    # Iniciar la aplicación Flask en el puerto 4850
    app.run(port=4850)
