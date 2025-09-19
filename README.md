# URL Shortener 🔗

A simple **URL Shortener** built with **Python Django**.  
This application allows you to shorten long URLs into simple, easy-to-share links and also provides QR codes for quick access.  

---

## 🚀 Features
- Shorten long URLs into unique short codes.  
- Redirect users from the short code to the original URL.  
- Generate **QR codes** for shortened links.  
- User-friendly interface with Django templates.  
- Powered by Django, Gunicorn, and SQLite/PostgreSQL.  

---

## 🛠️ Tech Stack
- **Backend:** Django 4.2  
- **Database:** SQLite (default) / PostgreSQL (optional)  
- **Deployment:** Gunicorn  
- **Utilities:** Pillow, qrcode, pypng  

---

## 📦 Requirements

The project dependencies are listed in `requirements.txt`: <br>
asgiref==3.8.1 <br>
backports.zoneinfo==0.2.1 <br>
colorama==0.4.6 <br>
Django==4.2.23 <br>
gunicorn==23.0.0 <br>
packaging==25.0 <br>
pillow==10.4.0 <br>
pypng==0.20220715.0 <br>
qrcode==7.4.2 <br>
sqlparse==0.5.3 <br>
typing_extensions==4.13.2 <br>
tzdata==2025.2 <br>

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/urlshortener.git
   cd urlshortener

2. **Create a virtual environment**
     ```bash
      python -m venv venv
      source venv/bin/activate    # Linux/Mac
      venv\Scripts\activate       # Windows

3. **Install dependencies**
     ```bash
      pip install -r requirements.txt
     
4. **Apply migrations**
     ```bash
      python manage.py migrate

5. **Run development server**
     ```bash
      python manage.py runserver

5. **Open in browser**
     ```bash
      http://127.0.0.1:8000/

---

## 📸 Screenshots
