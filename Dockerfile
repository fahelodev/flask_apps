# Usar la imagen oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias necesarias para la compilación
RUN apt-get update && apt-get install -y \
    libmariadb-dev \
    gcc \
    default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*  # Limpieza del cache de apt para reducir tamaño de la imagen

# Copiar todos los archivos necesarios al contenedor
COPY . /app

# Instalar dependencias de Python
# Asegúrate de tener un archivo requirements.txt en tu directorio con todas las dependencias necesarias
RUN pip install -r requirements.txt

# Exponer el puerto donde Flask correrá
# Flask por defecto corre en el puerto 5000
EXPOSE 8080

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
