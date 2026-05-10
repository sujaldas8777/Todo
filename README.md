# Todo Backend API – Secure Task Management with JWT Authentication

This README provides a complete guide to setting up and executing the Todo Backend API, a secure and scalable backend application that enables authenticated users to manage personal tasks using JWT-based authentication and authorization.

# Database

The project uses PostgreSQL for storing:

* User information
* Hashed passwords
* Todo tasks
* User-specific todo relationships

Ensure PostgreSQL is installed and running before execution.

## Step-by-Step Execution Instructions

### 1. Install Dependencies

Before running the project, ensure you have Python 3.10 or higher installed.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

### 2. Configure the Database

Create a PostgreSQL database:

```sql
CREATE DATABASE Todo_db;
```

Open the database configuration file and update your PostgreSQL credentials:

```python
DATABASE_URL = "postgresql://postgres:password@localhost:5432/Todo_db"
```

Replace:

* `postgres` → your PostgreSQL username
* `password` → your PostgreSQL password

### 3. Run the Complete Backend Server

To execute the complete backend application, run:

```bash
uvicorn app.main:app --reload
```

The server will start at:

```text
http://127.0.0.1:8000
```

### 4. Access Swagger Documentation

Open Swagger UI in your browser:

```text
http://127.0.0.1:8000/docs
```

The system will:

* Register new users securely using hashed passwords.
* Authenticate users using JWT-based login authentication.
* Authorize protected routes using Bearer tokens.
* Perform user-specific CRUD operations for todo management.
* Restrict users from accessing other users’ data.
* Validate request and response data using Pydantic schemas.
* Optimize database interactions using SQLAlchemy ORM and connection pooling.

## Troubleshooting

* Ensure PostgreSQL service is running correctly.
* Verify that database credentials and connection URL are correct.
* Activate the virtual environment before execution.
* Ensure all dependencies are installed properly via requirements.txt.
* Restart the server after updating dependencies.
* Recreate database tables if schema changes are made.
