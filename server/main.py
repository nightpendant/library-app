# placeholder API

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pprint import pprint


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Book:
    def __init__(self, id=1, name="The Bible", borrower="Simone C. Torres", avg_rating=4.3):
        self.id = id
        self.name = name
        self.borrowers = borrower
        self.avg_rating = avg_rating

books = []
books.append(Book())
books.append(Book(2, "The Stranger", "Ridge V. Reodique", 4.5))
books.append(Book(3, "Stranger Things", "", 4.5))

@app.post("/book")
async def return_book(id):
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
