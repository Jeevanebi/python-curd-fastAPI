# FastAPI CRUD Application with SQL Server

This project is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI, pyodbc, and SQL Server. The application allows you to manage user records in a SQL Server database.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install fastapi uvicorn pyodbc
    ```

## Setup

1. **Configure the database connection:**

    Update the `connection_string` in `main.py` with your SQL Server details.

    ```python
    server = 'your_server'
    database = 'TestDB'
    username = 'your_username'
    password = 'your_password'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    ```

2. **Ensure your SQL Server database has the necessary table:**

    ```sql
    CREATE TABLE test (
        EmpID INT PRIMARY KEY,
        Name NVARCHAR(100),
        Address NVARCHAR(100),
        Phone NVARCHAR(15)
    );
    ```

## Running the Application

Start the FastAPI application using Uvicorn:

```sh
uvicorn main:app --reload
```

This will start the application and make it available at `http://127.0.0.1:8000`.

## API Endpoints

### Create User

- **URL:** `/users/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "empId": 1,
        "name": "John Doe",
        "address": "123 Main St",
        "phone": "123-456-7890"
    }
    ```
- **Response:**
    ```json
    {
        "message": "User created successfully"
    }
    ```

### Read User

- **URL:** `/users/{id}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "EmpId": 1,
        "Name": "John Doe",
        "Address": "123 Main St",
        "Phone": "123-456-7890"
    }
    ```

### Update User

- **URL:** `/users/{id}`
- **Method:** `PUT`
- **Request Body:**
    ```json
    {
        "name": "John Doe",
        "address": "123 Main St",
        "phone": "123-456-7890"
    }
    ```
- **Response:**
    ```json
    {
        "message": "User updated successfully"
    }
    ```

### Delete User

- **URL:** `/users/{id}`
- **Method:** `DELETE`
- **Response:**
    ```json
    {
        "message": "User deleted successfully"
    }
    ```

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [pyodbc](https://github.com/mkleehammer/pyodbc)

## License

This project is licensed under the MIT License.
