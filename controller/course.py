from fastapi import APIRouter, Depends, HTTPException, Request, Response
from middleware.check_user import check_cookie_login
from models.course_model import Course
from repositorys.course_repo import CourseRepository
from services.course_service import CourseService

# prefix /course

router_course = APIRouter()
router = router_course

course_service = CourseService(CourseRepository())


# response=Depends(check_cookie_login)


@router.get("/")
async def index():
    course_all = course_service.get_course_all()
    return course_all


@router.post("/add-course")
async def add_course(course: Course, response=Depends(check_cookie_login)):
    status = response
    if status["status"] == "fail":
        return status
    add_course = course_service.add_course(course)
    return add_course


@router.patch("/edit-course/{id}")
async def edit_course(id, course: Course, response=Depends(check_cookie_login)):
    status = response
    if status["status"] == "fail":
        return status
    edit_course = course_service.edit_course(id, course)
    return edit_course


@router.get("/get-course/{id}")
async def get_course(id, response=Depends(check_cookie_login)):
    status = response
    if status["status"] == "fail":
        return status
    course = course_service.get_course(id)
    return course


@router.delete("/delete-course/{id}")
async def delete_course(id):
    delete_course = course_service.delete_course(id)
    return delete_course
