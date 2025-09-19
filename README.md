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

The project dependencies are listed in `requirements.txt`:
asgiref==3.8.1
backports.zoneinfo==0.2.1
colorama==0.4.6
Django==4.2.23
gunicorn==23.0.0
packaging==25.0
pillow==10.4.0
pypng==0.20220715.0
qrcode==7.4.2
sqlparse==0.5.3
typing_extensions==4.13.2
tzdata==2025.2

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/urlshortener.git
   cd urlshortener
