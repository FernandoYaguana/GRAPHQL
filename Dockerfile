# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios (como app.py y requirements.txt)
COPY . /app

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará la aplicación (por ejemplo, 5000)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]