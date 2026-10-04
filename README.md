# Student CRUD API

A simple **Student CRUD API** built using **Python and FastAPI**.

This project demonstrates how to create REST APIs for managing student information using:

- Python
- FastAPI
- Pydantic
- Uvicorn
- Swagger UI
- Postman
- Git and GitHub

---

## 1. Project Objective

The objective of this project is to build a FastAPI application that allows users to:

- Create a student
- View all students
- View a student by ID
- Update a student
- Delete a student

The application uses an in-memory Python list as the database.

---

## 2. Student Fields

Each student contains the following fields:

| Field | Type | Validation |
|---|---|---|
| id | Integer | Greater than 0 |
| name | String | 2-50 characters |
| email | Email | Valid email format |
| age | Integer | 5-100 |
| course | String | 2-100 characters |

Example:

```json
{
  "id": 1,
  "name": "Ravi Kumar",
  "email": "ravi@example.com",
  "age": 20,
  "course": "Python"
}
```

---

## 3. Project Structure

```text
student-crud-api/
│
├── main.py
├── requirements.txt
└── README.md
```

### main.py

Contains:

- FastAPI application
- Pydantic Student model
- In-memory student database
- CRUD API implementations
- Validation
- Error handling

### requirements.txt

Contains the Python dependencies required by the application.

### README.md

Contains project documentation, API details, testing instructions, and GitHub submission information.

---

## 4. Installation

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Go to the project directory

```bash
cd student-crud-api
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the Application

Run:

```bash
uvicorn main:app --reload
```

The application will start at:

```text
http://127.0.0.1:8000
```

---

# 6. Swagger UI

FastAPI automatically provides Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to execute and test all APIs.

Available APIs:

```text
POST    /students
GET     /students
GET     /students/{student_id}
PUT     /students/{student_id}
DELETE  /students/{student_id}
```

---

# 7. API Testing Using Swagger UI

## API 1: Create Student

### Endpoint

```text
POST /students
```

### Request

```json
{
  "id": 1,
  "name": "Ravi Kumar",
  "email": "ravi@example.com",
  "age": 20,
  "course": "Python"
}
```

### Expected Response

```json
{
  "id": 1,
  "name": "Ravi Kumar",
  "email": "ravi@example.com",
  "age": 20,
  "course": "Python"
}
```

### Status Code

```text
201 Created
```

### Swagger Steps

1. Open `/docs`.
2. Expand `POST /students`.
3. Click `Try it out`.
4. Enter the JSON request.
5. Click `Execute`.
6. Verify the response.
7. Verify the status code is `201`.

---

# 8. API 2: Get All Students

### Endpoint

```text
GET /students
```

### Swagger Steps

1. Expand `GET /students`.
2. Click `Try it out`.
3. Click `Execute`.

### Expected Response

```json
[
  {
    "id": 1,
    "name": "Ravi Kumar",
    "email": "ravi@example.com",
    "age": 20,
    "course": "Python"
  }
]
```

### Status Code

```text
200 OK
```

---

# 9. API 3: Get Student By ID

### Endpoint

```text
GET /students/{student_id}
```

### Example

```text
GET /students/1
```

### Swagger Steps

1. Expand `GET /students/{student_id}`.
2. Click `Try it out`.
3. Enter:

```text
1
```

4. Click `Execute`.

### Expected Response

```json
{
  "id": 1,
  "name": "Ravi Kumar",
  "email": "ravi@example.com",
  "age": 20,
  "course": "Python"
}
```

### Status Code

```text
200 OK
```

### Student Not Found Test

Try:

```text
999
```

Expected:

```json
{
  "detail": "Student not found"
}
```

Status:

```text
404 Not Found
```

---

# 10. API 4: Update Student

### Endpoint

```text
PUT /students/{student_id}
```

### Example

```text
PUT /students/1
```

### Request

```json
{
  "id": 1,
  "name": "Ravi Kumar Updated",
  "email": "ravi.updated@example.com",
  "age": 21,
  "course": "FastAPI"
}
```

### Swagger Steps

1. Expand `PUT /students/{student_id}`.
2. Click `Try it out`.
3. Enter student ID:

```text
1
```

4. Enter the request body.
5. Click `Execute`.

### Expected Status

```text
200 OK
```

---

# 11. API 5: Delete Student

### Endpoint

```text
DELETE /students/{student_id}
```

### Example

```text
DELETE /students/1
```

### Swagger Steps

1. Expand `DELETE /students/{student_id}`.
2. Click `Try it out`.
3. Enter:

```text
1
```

4. Click `Execute`.

### Expected Status

```text
204 No Content
```

The student will be removed from the in-memory database.

---

# 12. Pydantic Validation

The application uses Pydantic for request validation.

Example invalid request:

```json
{
  "id": -1,
  "name": "A",
  "email": "invalid-email",
  "age": 2,
  "course": "P"
}
```

This request is rejected because:

- ID must be greater than 0.
- Name must contain at least 2 characters.
- Email must have a valid email format.
- Age must be between 5 and 100.
- Course must contain at least 2 characters.

FastAPI returns:

```text
422 Unprocessable Entity
```

---

# 13. Error Handling

The API handles common errors.

### Student does not exist

```text
404 Not Found
```

Response:

```json
{
  "detail": "Student not found"
}
```

### Duplicate Student ID

```text
409 Conflict
```

Response:

```json
{
  "detail": "Student with this ID already exists"
}
```

### Duplicate Email

```text
409 Conflict
```

Response:

```json
{
  "detail": "Student with this email already exists"
}
```

---

# 14. Testing Using Postman

The APIs can also be tested using Postman.

Base URL:

```text
http://127.0.0.1:8000
```

## POST

Method:

```text
POST
```

URL:

```text
http://127.0.0.1:8000/students
```

Body → raw → JSON:

```json
{
  "id": 1,
  "name": "Ravi Kumar",
  "email": "ravi@example.com",
  "age": 20,
  "course": "Python"
}
```

Expected:

```text
201 Created
```

---

## GET All

Method:

```text
GET
```

URL:

```text
http://127.0.0.1:8000/students
```

Expected:

```text
200 OK
```

---

## GET By ID

Method:

```text
GET
```

URL:

```text
http://127.0.0.1:8000/students/1
```

Expected:

```text
200 OK
```

---

## PUT

Method:

```text
PUT
```

URL:

```text
http://127.0.0.1:8000/students/1
```

Body:

```json
{
  "id": 1,
  "name": "Ravi Kumar Updated",
  "email": "ravi.updated@example.com",
  "age": 21,
  "course": "FastAPI"
}
```

Expected:

```text
200 OK
```

---

## DELETE

Method:

```text
DELETE
```

URL:

```text
http://127.0.0.1:8000/students/1
```

Expected:

```text
204 No Content
```

---

# 15. Code Logic Explanation

## FastAPI Application

```python
app = FastAPI()
```

Creates the FastAPI application.

---

## Pydantic Model

```python
class Student(BaseModel):
```

Defines the structure and validation rules for a student.

Pydantic automatically validates incoming JSON data.

---

## In-Memory Database

```python
students = []
```

A Python list is used as a temporary database.

Data will be lost when the application stops.

---

## Create Student

```python
students.append(student)
```

Adds the new student to the list.

Before adding, the code checks whether the student ID or email already exists.

---

## Get Students

```python
return students
```

Returns all students.

---

## Get Student By ID

The application loops through the student list and searches for the requested ID.

If found:

```python
return student
```

If not found:

```text
404 Not Found
```

---

## Update Student

The application searches for the student ID.

If found, the existing student is replaced:

```python
students[index] = updated_student
```

---

## Delete Student

The application searches for the student and removes it:

```python
students.pop(index)
```

If the student doesn't exist, it returns:

```text
404 Not Found
```

---

# 16. Git and GitHub Submission

## Step 1: Initialize Git

Inside the project folder:

```bash
git init
```

---

## Step 2: Add Files

```bash
git add .
```

---

## Step 3: Commit

```bash
git commit -m "Create Student CRUD API using FastAPI"
```

---

## Step 4: Create GitHub Repository

Go to GitHub and create a new repository.

Repository name:

```text
student-crud-api
```

Set it to **Public** if your assignment requires a public repository.

Do not add README from GitHub if you already created one locally.

---

## Step 5: Connect Local Repository to GitHub

Copy your GitHub repository URL.

Example:

```bash
git remote add origin https://github.com/YOUR_USERNAME/student-crud-api.git
```

Verify:

```bash
git remote -v
```

---

## Step 6: Rename Branch to Main

```bash
git branch -M main
```

---

## Step 7: Push to GitHub

```bash
git push -u origin main
```

---

# 17. Verify GitHub Repository

Open your GitHub repository.

You should see:

```text
student-crud-api
│
├── main.py
├── requirements.txt
└── README.md
```

Click `README.md` and verify that all instructions and API demonstrations are displayed correctly.

---

# 18. Final Submission

Submit your GitHub repository URL:

```text
https://github.com/YOUR_USERNAME/student-crud-api
```

Example:

```text
https://github.com/ramupalanki/student-crud-api
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

# 19. Final Checklist

Before submitting, verify:

- [ ] FastAPI application created
- [ ] POST `/students` implemented
- [ ] GET `/students` implemented
- [ ] GET `/students/{student_id}` implemented
- [ ] PUT `/students/{student_id}` implemented
- [ ] DELETE `/students/{student_id}` implemented
- [ ] Pydantic validation added
- [ ] Proper HTTP status codes used
- [ ] 404 error handling implemented
- [ ] Duplicate student validation implemented
- [ ] Swagger UI tested
- [ ] Postman testing instructions included
- [ ] Code explanation included
- [ ] README.md created
- [ ] Git repository initialized
- [ ] Code committed
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] GitHub repository URL ready for submission

---

## 20. Submission Format

```text
Student CRUD API

GitHub Repository:
https://github.com/YOUR_USERNAME/student-crud-api

Swagger UI:
http://127.0.0.1:8000/docs

Implemented APIs:
1. POST /students
2. GET /students
3. GET /students/{student_id}
4. PUT /students/{student_id}
5. DELETE /students/{student_id}

Testing:
Swagger UI and Postman

Status:
Completed
```