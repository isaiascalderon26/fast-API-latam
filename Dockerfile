# syntax=docker/dockerfile:1.2
FROM python:latest
# put you docker configuration here
# syntax=docker/dockerfile:1.2
FROM python:latest

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY challenge/api.py .
COPY requirements-dev.txt .
COPY requirements-test.txt .
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto al correr el contenedor
CMD ["python", "api.py"]

