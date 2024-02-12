from fastapi import Request, Response
from models.status import Status
from repositorys.lesson_repo import LessonRepository


class LessonService:
    def __init__(self, lesson_repository: LessonRepository) -> None:
        self.lesson_repository = lesson_repository

    def get_lesson_in_course_all(self, uid):
        lesson_all = self.lesson_repository.get_lesson_in_course_all(uid)
        print(lesson_all)
        if isinstance(lesson_all, dict):
            return {"status": "fail", "data": lesson_all["error"]}
        return Status(status="ok", data=[lesson_all])

    def get_lesson(self, uid):
        get_lesson = self.lesson_repository.get_lesson(uid)
        if isinstance(get_lesson, dict):
            return {"status": "fail", "data": get_lesson["error"]}
        if len(get_lesson) == 0:
            return {"status": "fail", "data": "data not found"}
        return Status(status="ok", data=get_lesson)
