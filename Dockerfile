# Archivo: Dockerfile

# Utilizar una imagen base oficial de Python basada en Alpine Linux
FROM python:3.11-alpine

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de dependencias
COPY requirements.txt ./

# Instalar las dependencias especificadas
RUN pip install  -r requirements.txt

# Copiar el archivo principal de la aplicación
COPY app.py ./

# Crear el directorio de datos donde se almacenará el contador
RUN mkdir -p /data

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Definir el comando predeterminado para ejecutar la aplicación
CMD [ "python", "app.py" ]
