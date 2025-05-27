# Sportoviště Rezervace - Django Projekt

Tento projekt slouží pro správu sportovišť a jejich rezervací.

---

## Požadavky

- Python 3.8 a vyšší  
- Django (viz `requirements.txt`)  
- Další závislosti viz `requirements.txt`

---

## Instalace

1. Naklonujte repozitář:

   ```bash
   git clone <url_projektu>
   cd <adresář_projektu>

2. Vytvořte a aktivujte virtuální prostředí:
 ```bash
python3 -m venv venv
source venv/bin/activate
```

3. Nainstalujte závislosti:
Django>=4.2,<5.0
django-ninja>=0.19.0
pydantic>=2.0

4. Proveďte migrace databáze
```bash
python manage.py migrate
```

5. Vytvořte superuživatele (admin):
```bash
python manage.py createsuperuser
```

6. Spusťte vývojový server:
```bash
python manage.py runserver 
```
7. Otevřete aplikaci
http://127.0.0.1:8000/