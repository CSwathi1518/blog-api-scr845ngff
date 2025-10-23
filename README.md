# ✨ Blog API - SCR845NGFF 📝

A **RESTful API** for a blog application built with **Flask**, featuring **user authentication**, **posts**, and **comments**.

---

## 🚀 Features

- 🔐 User authentication (Register & Login)  
- 📰 CRUD operations for blog posts  
- 💬 Comment system for user interaction  
- 🧰 Environment-based configuration  
- 🗄️ Database migrations using Flask-Migrate  

---

## ⚙️ Setup Instructions

### 1️⃣ Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables  
Create a **.env** file in the project root and include necessary environment variables (e.g., `SECRET_KEY`, `DATABASE_URL`).

### 4️⃣ Initialize the Database  
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5️⃣ Run the Application 🚦  
```bash
python run.py
```

---

## 🌐 API Endpoints

### 🔑 Authentication
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/api/auth/register` | Register a new user 🆕 |
| POST | `/api/auth/login` | Login user 🔓 |

### 📝 Posts
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/api/posts` | Get all posts 📚 |
| POST | `/api/posts` | Create new post ✍️ |
| GET | `/api/posts/{id}` | Get single post 🔍 |
| PUT | `/api/posts/{id}` | Update post ⚙️ |
| DELETE | `/api/posts/{id}` | Delete post 🗑️ |

### 💬 Comments
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/api/comments` | Create comment 💡 |
| GET | `/api/comments?post_id={id}` | Get comments for a post 🧩 |
| PUT | `/api/comments/{id}` | Update comment 📝 |
| DELETE | `/api/comments/{id}` | Delete comment ❌ |

---

## 🧑‍💻 Tech Stack
- 🐍 Python (Flask)
- 🗃️ PostgreSQL / SQLite
- 🔁 SQLAlchemy ORM
- 🧩 Flask-Migrate
- 🔒 JWT Authentication

---

## 📜 License
This project is licensed under the **MIT License**.
