# 🤖 AI Blog Studio

AI Blog Studio is a full-stack Django REST API project that enables users to create, manage, and generate AI-powered blogs using Google's Gemini AI. The application provides secure authentication, blog management, category organization, and intelligent content generation through REST APIs.

---

## 🚀 Features

### 🔐 Authentication
- User Registration
- User Login (JWT Authentication)
- Refresh Token
- Protected APIs

### 📝 Blog Management
- Create Blog
- Update Blog
- Delete Blog
- View Single Blog
- List All Blogs

### 🤖 AI Blog Generation
- Generate professional blogs using **Google Gemini 3.5 Flash**
- Automatic title extraction
- Automatically saves generated blogs into the database
- Markdown formatted content
- Draft status support

### 📂 Categories
- Create Categories
- Assign category to blogs
- Category validation
- Filter blogs by category

### 🔍 Search & Filtering
- Search blogs by title
- Search blogs by content
- Filter by category
- Filter by status
- Ordering by title and creation date

### 🔒 Permissions
- JWT Protected APIs
- Only authors can edit or delete their own blogs

---

# 🛠 Tech Stack

### Backend
- Python
- Django
- Django REST Framework

### Database
- MySQL

### Authentication
- JWT (SimpleJWT)

### AI
- Google Gemini 3.5 Flash API

### Other Libraries
- django-filter
- Pillow
- python-dotenv

---

# 📂 Project Structure

```
AI-Blog-Studio/
│
├── accounts/
├── blogs/
├── config/
├── media/
├── requirements.txt
├── manage.py
└── README.md
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/aryaansaini/AI-Blog-Studio.git
```

```bash
cd AI-Blog-Studio
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a **.env** file

```env
SECRET_KEY=your_secret_key

DEBUG=True

GEMINI_API_KEY=your_gemini_api_key

DB_NAME=your_database

DB_USER=root

DB_PASSWORD=your_password

DB_HOST=localhost

DB_PORT=3306
```

### Run Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

# 📡 API Endpoints

## Authentication

```
POST /api/accounts/register/
POST /api/accounts/login/
POST /api/accounts/token/refresh/
```

## Blogs

```
POST   /api/blogs/
GET    /api/blogs/all/
GET    /api/blogs/<id>/
PUT    /api/blogs/<id>/
DELETE /api/blogs/<id>/
```

## AI

```
POST /api/blogs/generate/
```

Example

```json
{
    "topic":"Artificial Intelligence",
    "category":1
}
```

## Categories

```
GET  /api/blogs/categories/
POST /api/blogs/categories/
```

---

# 📷 Sample Response

```json
{
    "message":"Blog generated successfully",
    "id":12,
    "title":"Artificial Intelligence",
    "status":"draft"
}
```

---

# 🔐 Authentication

All protected APIs require

```
Authorization: Bearer <access_token>
```

---

# 📌 Current Features

- JWT Authentication
- Blog CRUD
- AI Blog Generation
- Category Management
- Search
- Filtering
- Ordering
- Author Permission
- Auto Save AI Blogs
- MySQL Database
- RESTful APIs

---

# 🚀 Future Enhancements

- React Frontend
- AI Image Generation
- Blog Slug URLs
- Reading Time
- Word Count
- AI Summary
- Tags Generation
- Rich Text Editor
- Blog Likes & Comments
- Deployment (Render + Vercel)

---

# 👨‍💻 Author

**Aryan Saini**

Python Backend Developer | Django | Django REST Framework | AI Integration | REST APIs | MySQL | Google Gemini AI

---

GitHub: https://github.com/aryaansaini

LinkedIn: https://www.linkedin.com/in/aryaansaini/