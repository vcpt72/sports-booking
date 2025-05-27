# SportBooking – Systém pro správu sportovišť a rezervací

Webová aplikace umožňující správu sportovišť, vytváření uživatelských účtů, rezervace termínů a hodnocení sportovišť.

## 🔧 Funkce aplikace

- Registrace a přihlášení uživatelů
- Rezervace sportovišť na zvolený den a čas
- Správa rezervací (vytváření, úprava, mazání)
- Uživatelský profil
- Hodnocení sportovišť (1–5 hvězdiček + recenze)
- Admin rozhraní pro správu obsahu
- REST API pomocí Django Ninja

---

## 🧰 Použité technologie

- Python 3.11+
- Django 4.x
- SQLite (výchozí databáze)
- Django Ninja (pro REST API)
- Bootstrap 5 (pro frontend)
- Pydantic 2.x (přes Django Ninja)
- Pillow (pro obrázky)

---

## 🚀 Instalace projektu

1. **Naklonuj repozitář**

```bash
git clone https://github.com/uzivatel/sportrezerva.git
cd sportrezerva
```
2. **Vytvoř a aktivuj virtuální prostředí**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. **Nainstaluj závislosti**
```bash
pip install -r requirements.txt
```
4. **Spusť migrace**
```bash
python manage.py migrate
```
5. **Vytvoř superuživatele (admina)**
```bash
python manage.py createsuperuser
```
6. **Spusť server**
```bash
python manage.py runserver
```

🔐 **Přístup do adminu**
```url
http://127.0.0.1:8000/admin
```
![image](https://github.com/user-attachments/assets/60e56584-99d6-49fc-9dde-f97ff9f89c3a)

![image](https://github.com/user-attachments/assets/7e8998d2-74ad-46c5-a4ab-d255b3adef24)


![image](https://github.com/user-attachments/assets/51e5d8bb-115f-438a-9b73-d2c93c80627a)

![image](https://github.com/user-attachments/assets/62578082-e586-4c15-ad24-3cc71cdeb1ba)

