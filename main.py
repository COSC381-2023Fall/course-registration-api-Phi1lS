from fastapi import FastAPI, HTTPException
from typing import List
from course import Course, courses
from student import Student
from pydantic import BaseModel

class CourseCreate(BaseModel):
    prefix: str
    course_number: str
    cap: int
    instructor: str
    name: str
    place: str
    meeting_times: str

app = FastAPI()

students = {}

@app.get("/courses/{prefix}")
def get_courses(prefix: str):
    # Return all the courses under the prefix
    results = []
    for course in courses:
        if course.is_prefix(prefix):
            course_data = {
                "prefix": course._prefix,
                "course_number": course._course_number,
                "name": course._name,
                "instructor": course._instructor,
                "place": course._place,
                "meeting_times": course._meeting_times
            }
            results.append(course_data)
    return results

@app.get("/students/{eid}/courses")
def get_student_courses(eid: str):
    student = students.get(eid)
    if student:
        # Serialize courses data for the response
        registered_courses = [
            {
                "prefix": course._prefix,
                "course_number": course._course_number,
                "name": course._name,
                "instructor": course._instructor,
                "place": course._place,
                "meeting_times": course._meeting_times
            }
            for course in student.registered_courses
        ]
        return registered_courses
    else:
        raise HTTPException(status_code=404, detail="Student not found")
    
@app.post("/students/{eid}/register_course/")
def register_course_to_student(eid: str, course_data: CourseCreate):
    student = students.get(eid)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    new_course = Course(**course_data.dict())

    student.register_course(new_course)
    return {"message": "Course registered successfully"}