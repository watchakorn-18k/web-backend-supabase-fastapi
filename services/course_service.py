from fastapi import Request, Response
from models.course_model import Course
from models.status import Status
from repositorys.user_repo import UserRepository


class CourseService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def get_course_all(self):
        course_all = self.user_repository.get_course_all()
        if course_all == "error":
            return Status(status="fail", data=course_all)
        return Status(status="ok", data=[Course(**course) for course in course_all])

    def add_course(self, course: Course):
        add_course = self.user_repository.add_course(course)
        if add_course == "error":
            return Status(status="fail", data=add_course)
        return Status(status="ok", data=add_course)
