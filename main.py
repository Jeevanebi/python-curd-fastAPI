from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
import pyodbc

app = FastAPI()

# Database connection setup
server = 'your_server'
database = 'TestDB'
username = 'your_username'
password = 'your_password'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Pydantic model
class User(BaseModel):
    empId: int
    name: str
    address: str
    phone: int

def get_db_connection():
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print("Connection Error: ", e)
        return None


# Get All Users
@app.get("/users/")
def read_all_user():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute("SELECT EmpId, Name, Address, Phone FROM test")
    rows = cursor.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

# Get Users by ID
@app.get("/users/{id}")
def read_user(id: int = Path(..., description="The ID of the user to retrieve")):
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute("SELECT EmpId, Name, Address, Phone FROM test WHERE EmpId = ?", id)
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(zip([column[0] for column in cursor.description], row))
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Create a New User
@app.post("/users/")
def create_user(user: User):
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO test (EmpID, Name, Address, Phone) VALUES (?, ?, ?, ?)",
        (user.empId, user.name, user.address, user.phone)
    )
    conn.commit()
    conn.close()
    return {"message": "User created successfully"}

# Update an Existing User Based on EmpId
@app.put("/users/{id}")
def update_user(id: int, user: User):
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE test SET Name = ?, Address = ?, Phone = ? WHERE EmpId = ? ",
        (user.name, user.address, user.phone, id)
    )
    conn.commit()
    conn.close()
    return {"message": "User updated successfully"}

# Delete an Existing User on EmpId
@app.delete("/users/{id}")
def delete_user(id: int):
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM test WHERE EmpId = ?", id)
    conn.commit()
    conn.close()
    return {"message": "User deleted successfully"}

# Define a port
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
