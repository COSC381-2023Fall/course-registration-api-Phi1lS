from student import Student
from course import Course
import pytest

@pytest.fixture
def student():
    return Student("EID123", "John Doe")

@pytest.fixture
def courseA():
    return Course("COSC", "111", 30, "John Doe", "Programming I", "PH 503", "TH 9:00")

def test_confirmation_mocked(mocker, courseA):
    # Mock confirmation method in Course
    mocker.patch.object(courseA, 'confirmation', return_value=None)

    # Calling request_for_changing_room should not trigger actual sleep
    courseA.request_for_changing_room("New Room 101")
    assert courseA._place == "New Room 101"