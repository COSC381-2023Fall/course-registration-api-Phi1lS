from fastapi.testclient import TestClient
from main import app, students
from course import Course, courses
from student import Student

client = TestClient(app)

def test_get_courses():
    courseA = Course("COSC", "111", 30, "John Doe", "Programming I", "PH 503", "TH 9:00")
    courses.append(courseA)
    
    response = client.get("/courses/COSC")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['prefix'] == 'COSC'
    assert response.json()[0]['course_number'] == '111'

    courses.remove(courseA)

def test_get_student_courses():
    student = Student("EID123", "John Doe")
    courseA = Course("COSC", "111", 30, "John Doe", "Programming I", "PH 503", "TH 9:00")
    student.register_course(courseA)
    students["EID123"] = student

    response = client.get("/students/EID123/courses")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['prefix'] == 'COSC'
    assert response.json()[0]['course_number'] == '111'

    del students["EID123"]

def test_register_course_to_student():
    # Setup - create a student
    student = Student("EID123", "John Doe")
    students["EID123"] = student

    # Data for the course to register
    course_data = {
        "prefix": "COSC",
        "course_number": "111",
        "cap": 30,
        "instructor": "John Doe",
        "name": "Programming I",
        "place": "PH 503",
        "meeting_times": "TH 9:00"
    }

    # Make the POST request
    response = client.post(f"/students/EID123/register_course/", json=course_data)

    # Check the response
    assert response.status_code == 200
    assert response.json() == {"message": "Course registered successfully"}

    # Check if the course was actually added to the student
    assert len(students["EID123"].registered_courses) == 1
    assert students["EID123"].registered_courses[0]._prefix == "COSC"
    assert students["EID123"].registered_courses[0]._course_number == "111"

    # Clear memory
    del students["EID123"]