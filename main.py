from fastapi import FastAPI
from course import courses

app = FastAPI()


@app.get("/courses/{prefix}")
def get_courses(prefix: str):
    # return all the courses under the prefix
    results = []
    for course in courses:
        if course.is_prefix(prefix):
            results.append(course)
    
    return results