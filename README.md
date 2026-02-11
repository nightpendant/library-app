# Current Architecture:

    ## Types of Data Stored:
        - Users
        - Books
        - Reviews/Ratings
        - Borrow Requests
        - Tags

    ## API:
        - POST   /auth/login
        - GET    /books
        - GET    /books/{id}
        - POST   /reviews/books/{book_id}
        - DELETE /reviews/{review_id}
        - POST   /tags/books/{book_id}
        - DELETE /tags/{tag_id}

    ## Process of Handling Request:
        
        User Sends HTTP Request -> Request gets handled by appropriate Router code -> Data validated by service code -> Database updated using repository code
         
