from fastapi import APIRouter, Depends, HTTPException, Request, Response
from middleware.check_user import check_cookie_login
from services.lesson_serivce import LessonService
from repositorys.lesson_repo import LessonRepository

# prefix /course/lesson

router_lesson = APIRouter()
router = router_lesson

lesson_service = LessonService(LessonRepository())


@router.get("/")
async def get_lesson_all():
    lesson_all = lesson_service.get_lesson_all()
    return lesson_all


@router.get("/{uid}")
async def get_lesson(uid: str):
    lesson = lesson_service.get_lesson(uid)
    return lesson
