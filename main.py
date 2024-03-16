from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import User
from database import Database

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

db = Database("db.sqlite3")
db.open_connection()

@app.post("/post/form")
async def create_user(User: User):
    query = f"INSERT INTO users (fname, lname) VALUES ('{User.fname}', '{User.lname}')"
    db.execute_query(query)
    return {"message": "Inserted successfully"}

@app.get("/get/form")
async def create_user(fname: str, lname: str):
    query = f"INSERT INTO users (fname, lname) VALUES ('{fname}', '{lname}')"
    db.execute_query(query)
    return {"message": "Inserted successfully"}

@app.get("/get/all")
async def read_users():
    query = "SELECT * FROM users"
    rows = db.execute_query(query)
    return {"users": rows}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)