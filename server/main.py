# placeholder API

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pprint import pprint

from pydantic_core.core_schema import IncExDictOrElseSerSchema


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "null"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Book:
    def __init__(self, id=1, title="The Bible", author="Yahweh", genre="Religious Texts", borrower="Simone C. Torres", avg_rating=4.3):
        self.id = id
        self.title = title
        self.borrower = borrower
        self.author=author
        self.genre = genre
        self.avg_rating = avg_rating

class User:
    def __init__(self, id=1, email="rnsagum@cbzrc.pshs.edu.ph", password="password"):
        self.id = id 
        self.email = email
        self.password = password

books = []
books.append(Book())
books.append(Book(2, "The Stranger", "Albert Camus", "Absurdist Literature", "Ridge V. Reodique", 4.5))
books.append(Book(3, "Perfect Strangers", "J.T. Geissinger", "Romance", "", 4.5))

book_of_the_day = Book(67, "Atlas Shrugged", "Ayn Rand", "Misinformation", "Sky N. Cartano", 5.0)

@app.post("/book")
async def return_book(id):
    if id == "day":
        return book_of_the_day.__dict__

    id = int(id)
    pprint(id)
    found_book = books[id]
    return found_book.__dict__

@app.post("/search")
async def return_search_results(type, query):
    results = []
    print("Type: ", type)
    print("Query: ", query)
    match type:
        case "books":
            for b in books:
                pprint(b.name)
                if query.lower() in b.name.lower():
                    print("Found ", query, "!")
                    results.append(b)
        case "users":
            return "Not Yet Okay"
        case "lists":
            return "Not Yet Okay"
        case _:
            raise HTTPException(status_code=404, detail="Requested type is not searchable!")

    pprint(results)
    return results

