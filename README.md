# 🔗 Minimal URL Shortener API (Django REST Framework)

Simple URL shortener API built with Django REST Framework.

---

## ✨ Features

- **Shorten long URLs** via a POST request.
- **Expand shortened URLs** via a GET request using the short code.
- **No duplicate entries** – existing URLs return their previous short code.

---

## 🚀 Quickstart

### 1. Clone the repository:
```bash
git clone https://github.com/Ezg0t/simple-URL-shortener
cd url-shortener
```
### 2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
### 4. Run migrations and start the server:
```bash
python manage.py migrate
python manage.py runserver
```
## 📚 API Endpoints

### `POST /shorten/` – Shorten a long URL

Creates a short URL for the given long URL.

#### Request Body:

```json
{
  "url": "https://example.com/very/long/path"
}
```
Successful Response:
```json
{
  "short_url": "http://127.0.0.1:8000/shrt/kr1fFJ/"
}
```

### `GET /shrt/<short_code>/` – Expand a short URL

Example request: GET http://127.0.0.1:8000/shrt/kr1fFJ/

Successful Response:
```json
{
  "url": "https://example.com/very/long/path"
}
```