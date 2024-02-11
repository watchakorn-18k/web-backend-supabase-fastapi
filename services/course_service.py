from fastapi import Request, Response
from models.course_model import Course
from models.status import Status
from repositorys.course_repo import CourseRepository


class CourseService:
    def __init__(self, course_repository: CourseRepository) -> None:
        self.course_repository = course_repository

    def get_course_all(self):
        course_all = self.course_repository.get_course_all()
        if course_all == "error":
            return Status(status="fail", data=course_all)
        return Status(status="ok", data=[Course(**course) for course in course_all])

    def add_course(self, course: Course):
        add_course = self.course_repository.add_course(course)
        if add_course == "error":
            return Status(status="fail", data=add_course)
        return Status(status="ok", data=add_course)

    def edit_course(self, id, course: Course):
        course.id = id
        edit_course = self.course_repository.edit_course(course)
        if edit_course == "error":
            return Status(status="fail", data=edit_course)
        return Status(status="ok", data=edit_course)

    def get_course(self, id):
        get_course = self.course_repository.get_course(id)
        if get_course == "error":
            return Status(status="fail", data=get_course)
        if len(get_course) == 0:
            return Status(status="fail", data=["data not found"])
        return Status(status="ok", data=get_course)
