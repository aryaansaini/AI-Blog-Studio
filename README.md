# 🤖 AI Blog Studio

An AI-powered Blog Management Platform built with **Django REST Framework**, **JWT Authentication**, **MySQL**, and **Google Gemini AI**. Users can securely create, manage, and generate AI-powered blog content through REST APIs.

---

## 🚀 Features

- 🔐 JWT Authentication (Register/Login/Refresh Token)
- 👤 Custom User Model & User Profile
- ✍️ Blog CRUD Operations
- 🤖 AI Blog Generation using Google Gemini 3.5 Flash
- 📂 Blog Categories
- 🔍 Search Blogs
- 🎯 Filter Blogs by Category & Status
- 📊 Ordering & Sorting
- 🖼️ Image Upload Support
- 🔒 Owner-Based Permissions
- 🗄️ MySQL Database
- 🌐 RESTful APIs

---

## 🛠️ Tech Stack

### Backend
- Python 3
- Django 5
- Django REST Framework

### Database
- MySQL

### Authentication
- JWT (Simple JWT)

### AI
- Google Gemini 3.5 Flash
- Google GenAI SDK

### Other Libraries
- django-filter
- Pillow
- python-decouple

---

## 📁 Project Structure

```
AI-Blog-Studio/
│── accounts/
│── blogs/
│── config/
│── media/
│── requirements.txt
│── manage.py
│── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Blog-Studio.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=your_database
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306

GEMINI_API_KEY=your_gemini_api_key
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

## 📌 API Endpoints

### Authentication

```
POST /api/accounts/register/
POST /api/accounts/login/
POST /api/accounts/token/refresh/
GET  /api/accounts/profile/
```

### Blogs

```
POST   /api/blogs/
GET    /api/blogs/all/
GET    /api/blogs/<id>/
PUT    /api/blogs/<id>/
DELETE /api/blogs/<id>/
```

### Categories

```
GET  /api/blogs/categories/
POST /api/blogs/categories/
```

### AI Blog Generation

```
POST /api/blogs/generate/
```

Request

```json
{
    "topic": "Artificial Intelligence"
}
```

---

## 🔒 Security

- JWT Authentication
- Owner-Based Authorization
- Protected API Endpoints
- Secure Environment Variables

---

## 🚀 Future Enhancements

- ❤️ Like & Bookmark Blogs
- 💬 Comments System
- 📄 PDF Export
- 🌍 Multi-language Translation
- 🤖 AI Blog Summarization
- 🧠 RAG (Retrieval-Augmented Generation)
- 📈 Blog Analytics Dashboard

---

## 👨‍💻 Author

**Aryan Saini**

Python Backend Developer | Django | REST APIs | AI Integration


GitHub: https://github.com/aryaansaini

LinkedIn: https://www.linkedin.com/in/aryaansaini/