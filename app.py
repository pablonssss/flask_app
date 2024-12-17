# Archivo: app.py
# Importamos las bibliotecas necesarias
from flask import Flask
import os

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Definimos la ruta del archivo donde se almacenará el contador de visitas
contador_file = '/data/contador.txt'

# Aseguramos que el directorio para el archivo de contador exista
os.makedirs(os.path.dirname(contador_file), exist_ok=True)

# Si el archivo de contador no existe, lo creamos e inicializamos en 0
if not os.path.exists(contador_file):
    with open(contador_file, 'w') as f:
        f.write('0')

# Definimos la ruta principal de la aplicación
@app.route('/')
def index():
    # Abrimos el archivo en modo lectura para obtener el valor actual del contador
    with open(contador_file, 'r') as f:
        contador = int(f.read())
    
    # Incrementamos el contador en 1
    contador += 1
    
    # Guardamos el nuevo valor del contador en el archivo
    with open(contador_file, 'w') as f:
        f.write(str(contador))
    
    # Devolvemos un mensaje mostrando el número actual de visitas
    return f'Visitas: {contador}'

# Ejecutamos la aplicación si se llama directamente este archivo
if __name__ == '__main__':
    # Configuramos Flask para ejecutarse en cualquier dirección IP y en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
