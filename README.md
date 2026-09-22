# Library API

A simple REST API built with **FastAPI** to manage a small collection of books.
Built as a beginner practice project to learn the core concepts of FastAPI: path parameters, query parameters, POST requests, error handling, and Pydantic models.

## Features

- View a welcome message
- Add a new book
- Get a single book by ID
- Search books by author
- Delete a book by ID

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — Python web framework
- [Uvicorn](https://www.uvicorn.org/) — ASGI server to run the app
- [Pydantic](https://docs.pydantic.dev/) — data validation

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/library-api.git
cd library-api
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn
```

### 3. Run the server

```bash
uvicorn main:library --reload
```

### 4. Try it out

Open your browser at:

```
http://127.0.0.1:8000/docs
```

This shows an interactive page where you can test every endpoint.

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Welcome message |
| POST | `/books` | Add a new book |
| GET | `/books/{book_id}` | Get a book by its ID |
| GET | `/search?author=NAME` | Search books by author |
| DELETE | `/books/{book_id}` | Delete a book by its ID |

### Example: Add a book

**Request:** `POST /books`

```json
{
  "id": 1,
  "title": "Calculus",
  "author": "Isaac Newton",
  "available": true
}
```

**Response:**

```json
{
  "message": "Your book 'Calculus' was added successfully",
  "book": {
    "id": 1,
    "title": "Calculus",
    "author": "Isaac Newton",
    "available": true
  }
}
```

## What I Learned

This project was built while learning FastAPI from scratch, covering:

- Path parameters (`/books/{book_id}`)
- Query parameters (`/search?author=...`)
- POST requests with Pydantic models
- Error handling with `HTTPException`
- The auto-generated `/docs` testing page

## Possible Next Steps

- Add input validation (e.g. reject empty titles)
- Connect to a real database instead of an in-memory list
- Add an update (`PUT`) endpoint