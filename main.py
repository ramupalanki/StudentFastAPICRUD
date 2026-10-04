from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from typing import List


app = FastAPI(
    title="Student CRUD API",
    description="A simple FastAPI application for managing students",
    version="1.0.0"
)


# -----------------------------
# Pydantic Model
# -----------------------------

class Student(BaseModel):
    id: int = Field(..., gt=0, description="Student ID must be greater than 0")
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=5, le=100)
    course: str = Field(..., min_length=2, max_length=100)


# -----------------------------
# In-memory database
# -----------------------------

students: List[Student] = []


# -----------------------------
# POST - Create Student
# -----------------------------

@app.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: Student):
    for existing_student in students:
        if existing_student.id == student.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Student with this ID already exists"
            )

        if existing_student.email == student.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Student with this email already exists"
            )

    students.append(student)

    return student


# -----------------------------
# GET - Get All Students
# -----------------------------

@app.get(
    "/students",
    response_model=List[Student]
)
def get_students():
    return students


# -----------------------------
# GET - Get Student By ID
# -----------------------------

@app.get(
    "/students/{student_id}",
    response_model=Student
)
def get_student(student_id: int):

    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


# -----------------------------
# PUT - Update Student
# -----------------------------

@app.put(
    "/students/{student_id}",
    response_model=Student
)
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student.id == student_id:

            if updated_student.id != student_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Student ID in request body must match URL student_id"
                )

            students[index] = updated_student

            return updated_student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


# -----------------------------
# DELETE - Delete Student
# -----------------------------

@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student.id == student_id:

            students.pop(index)

            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )