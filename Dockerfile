# Python 3.10 slim image
FROM python:3.10-slim

# Çalışma dizini
WORKDIR /app

# Uygulama dosyalarını kopyala
COPY app/app.py app/requirements.txt ./

# Gerekli paketleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Port aç
EXPOSE 5000

# Uygulamayı başlat
CMD ["python", "app.py"]
