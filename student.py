class Student:
    def __init__(self, eid, name):
        self.eid = eid
        self.name = name
        # Start registered courses as empty list
        self.registered_courses = []

    def register_course(self, course):
        # Check if course is a valid course
        if(course):
            # Check if the course is already registered
            if course not in self.registered_courses:
                self.registered_courses.append(course)
                return True
        return False

    def get_registered_courses_info(self):
        return [
            {
                "prefix": course._prefix,
                "course_number": course._course_number,
                "name": course._name,
                "instructor": course._instructor,
                "place": course._place,
                "meeting_times": course._meeting_times
            }
            for course in self.registered_courses
        ]