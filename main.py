from fastapi import FastAPI

fake_db = [
    {"id": 1, "name": "boris"},
    {"id": 2, "name": "cvas"},
    {"id": 11, "name": "tars"},
]

fake_trades = [ {"id": 1, "user_id": 11}, {"id": 2, "user_id": 2} ]

app = FastAPI(
    title="Work with DB"
)


@app.get("/user/{user_id}")
def get_user(user_id: int ):
    return [user for user in fake_db if user.get("id") == user_id]

@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[limit:][:offset]

@app.post("/users/{user_id}")
def add_new_user(user_id: int, name: str):
    fake_db.append({"id": user_id, "name": name})
    return {"status": 200, "data": fake_db}