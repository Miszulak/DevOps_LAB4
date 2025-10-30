# 1. Użyj oficjalnego obrazu Python jako bazy
FROM python:3.9-slim

# 2. Ustaw katalog roboczy w kontenerze
WORKDIR /app

# 3. Skopiuj plik zależności i je zainstaluj
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Skopiuj resztę kodu aplikacji
COPY . .

# 5. Ustaw domyślne polecenie uruchamiane przy starcie kontenera
CMD ["python", "app.py"]