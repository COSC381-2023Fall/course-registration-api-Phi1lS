from course import Course, courses
import pytest

@pytest.fixture
def courseA():
    courseA = Course("COSC", "111", 30, "John Doe", 
        "Programming I", "PH 503", "TH 9:00")
    return courseA
    
# def test_add_a_course(courseA):
#     courses.append(courseA)
#     assert len(courses) == 1

def test_is_prefix(courseA):
    assert courseA.is_prefix("COSC")
    assert not courseA.is_prefix("ABC")

def test_request_for_changing_room(courseA, mocker):
    mocker.patch(
        'course.Course.confirmation'
    )
    courseA.request_for_changing_room("New Place")
    assert courseA._place == "New Place"