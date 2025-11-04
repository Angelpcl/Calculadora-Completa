# Dockerfile

# Usa una imagen base de Python ligera
FROM python:3.11-slim

# Instala las dependencias del sistema operativo necesarias para Tkinter (GUI)
# Nota: 'python3-tk' proporciona la librería requerida.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-tk \
        # Limpieza de caché para mantener la imagen pequeña
        && apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias e instala los módulos Python
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu código de la calculadora
COPY src/calculator_gui.py .

# Define el comando para ejecutar la aplicación
CMD ["python", "calculator_gui.py"]