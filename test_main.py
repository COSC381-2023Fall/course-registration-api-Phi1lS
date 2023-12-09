from fastapi.testclient import TestClient
from main import app
from test_course import courseA
from course import courses

client = TestClient(app)

def test_get_courses(courseA):
    courses.append(courseA)

    response = client.get("/courses/COSC")
    assert response.status_code == 200
    assert response.json() == [
        {
            "_prefix":"COSC",
            "_course_number":"111",
            "_cap":30,
            "_instructor":"John Doe",
            "_name":"Programming I",
            "_place":"PH 503",
            "_meeting_times":"TH 9:00"
        }]

    courses.pop()