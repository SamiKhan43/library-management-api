from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

library = FastAPI()


@library.get("/")
def welcome_message():
    return {"message": "Welcome to the Library API"}


class Book(BaseModel):
    id: int
    title: str
    author: str
    available: bool


books = []


@library.post("/books")
def add_book(book: Book):
    books.append(book)

    return {
        "message": f"Your book '{book.title}' was added successfully",
        "book": book
    }


@library.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


@library.get("/search")
def search_books(author: str):
    result = []

    for book in books:
        if book.author == author:
            result.append(book)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="No books found for this author"
        )

    return result


@library.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)

            return {
                "message": f"Book '{book.title}' was deleted successfully",
                "book": book
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
 