import time

class Course:
    def __init__(self, prefix, course_number, cap, instructor, name, place, meeting_times):
        self._prefix = prefix
        self._course_number = course_number
        self._cap = cap
        self._instructor = instructor
        self._name = name
        self._place = place
        self._meeting_times = meeting_times 

    def is_prefix(self, prefix):
        return self._prefix == prefix

    def request_for_changing_room(self, new_place):
        # TODO: unfinished
        self.confirmation()
        self._place = new_place
    
    def confirmation(self):
        # Mock this method in testing
        # ask for confirmation from admin
        time.sleep(10) # to be finished

courses = []
