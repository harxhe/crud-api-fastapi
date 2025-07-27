# FastAPI CRUD API with PostgreSQL

This is a simple backend API built using **FastAPI** and **PostgreSQL**, created as part of a workshop hosted by IEEE Computer Society - VIT. It demonstrates basic **Create, Read, Update, and Delete (CRUD)** operations on a PostgreSQL database.

---

## Features

- RESTful API endpoints for CRUD operations
- PostgreSQL integration using SQLAlchemy ORM
- Pydantic models for data validation
- Auto-generated Swagger UI at `/docs`

---

## Tech Stack

| Layer              | Technology     | Purpose                                               |
|--------------------|----------------|--------------------------------------------------------|
| Backend Framework  | FastAPI        | Building fast, asynchronous REST APIs                  |
| Database           | PostgreSQL     | Storing and managing structured data                   |
| ORM                | SQLAlchemy     | Interacting with the database using Python objects     |
| Data Validation    | Pydantic       | Validating request and response models                 |
| Server             | Uvicorn        | ASGI server to run FastAPI apps                        |
| Environment Config | python-dotenv  | Loading environment variables from `.env` files        |
