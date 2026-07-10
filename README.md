# 🚀 AI Blog Studio

An AI-powered Blog Management REST API built with **Django REST Framework**. The project provides secure JWT authentication, blog management, categories, search, filtering, and role-based authorization. It is designed using RESTful API principles and follows a scalable backend architecture.

## ✨ Features

- 🔐 JWT Authentication (Register, Login, Refresh Token)
- 👤 Custom User Model & Profile API
- 📝 Blog CRUD Operations
- 🏷️ Category Management
- 🔒 Owner-Based Authorization
- 🔍 Search Blogs by Title & Content
- 📂 Filter Blogs by Status & Category
- ↕️ Ordering & Sorting Support
- 🖼️ Image Upload Support
- 🗄️ MySQL Database Integration
- ⚡ RESTful API using Django REST Framework
- 🤖 AI Blog Generation (Gemini Integration - In Progress)

---

## 🛠️ Tech Stack

- Python 3
- Django
- Django REST Framework
- MySQL
- JWT Authentication (SimpleJWT)
- Django Filter
- Google Gemini API (In Progress)
- Git & GitHub

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

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/aryaansaini/AI-Blog-Studio.git
cd AI-Blog-Studio
```

### Create Virtual Environment

```bash
python -m venv venv
```

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

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

DB_NAME=your_database
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306

GEMINI_API_KEY=your_api_key
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint |
|---------|----------|
| POST | `/api/accounts/register/` |
| POST | `/api/accounts/login/` |
| POST | `/api/accounts/token/refresh/` |
| GET | `/api/accounts/profile/` |

### Blogs

| Method | Endpoint |
|---------|----------|
| POST | `/api/blogs/` |
| GET | `/api/blogs/all/` |
| GET | `/api/blogs/<id>/` |
| PUT | `/api/blogs/<id>/` |
| DELETE | `/api/blogs/<id>/` |

### Categories

| Method | Endpoint |
|---------|----------|
| GET | `/api/blogs/categories/` |
| POST | `/api/blogs/categories/` |

### AI Blog Generator

| Method | Endpoint |
|---------|----------|
| POST | `/api/blogs/generate/` *(In Progress)* |

---

## 📸 Current Features

- Secure Authentication
- REST APIs
- Blog Management
- Category Management
- Search & Filtering
- Owner Permission
- MySQL Integration

---

## 🔮 Upcoming Features

- AI Blog Generation
- Swagger API Documentation
- Docker Support
- Deployment (Render/AWS)
- CI/CD Pipeline

---

## 👨‍💻 Author

**Aryan Saini**

GitHub: https://github.com/aryaansaini

LinkedIn: https://www.linkedin.com/in/aryaansaini/