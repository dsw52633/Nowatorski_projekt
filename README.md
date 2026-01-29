# Nowatorski Projekt Indywidualny – Study Tasks API

Projekt wykonany w ramach przedmiotu **Nowatorski Projekt Indywidualny**.  
Celem projektu było zaprojektowanie i wdrożenie środowiska DevOps umożliwiającego
budowanie, testowanie oraz uruchamianie aplikacji API w sposób zautomatyzowany.

## Opis projektu
Aplikacja **Study Tasks API** umożliwia zarządzanie zadaniami związanymi z nauką.
Dane aplikacji są przechowywane w bazie danych PostgreSQL, a całość jest uruchamiana
w środowisku kontenerowym.

Projekt demonstruje wykorzystanie narzędzi DevOps takich jak Docker, Docker Compose
oraz GitHub Actions.

## Wykorzystane technologie
- Python + FastAPI
- Docker (multi-stage Dockerfile)
- Docker Compose (aplikacja + baza danych)
- PostgreSQL
- GitHub Actions (Continuous Integration)
- Pytest

## Uruchomienie projektu
Wymagane: Docker oraz Docker Compose.

```bash
git clone https://github.com/dsw52633/Nowatorski_projekt.git
cd Nowatorski_projekt
docker compose up -d --build
Po uruchomieniu aplikacja dostępna jest pod adresem:

http://localhost:8000

Dokumentacja API (Swagger): http://localhost:8000/docs
