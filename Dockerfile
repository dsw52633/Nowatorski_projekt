# ETAP 1: Builder - instalujemy zależności
FROM python:3.9-slim as builder

WORKDIR /app

# Kopiujemy plik z wymaganiami
COPY requirements.txt .

# Instalujemy zależności do katalogu /install
# --no-cache-dir zmniejsza rozmiar obrazu
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ETAP 2: Finalny obraz uruchomieniowy
FROM python:3.9-slim

WORKDIR /app

# Kopiujemy tylko zainstalowane biblioteki z etapu builder
COPY --from=builder /install /usr/local

# Kopiujemy kod aplikacji
COPY . .

# Wystawiamy port (informacyjnie)
EXPOSE 8000

# Komenda startowa
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]