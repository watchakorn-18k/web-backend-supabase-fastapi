from controller.user import router_user
from controller.course import router_course
from fastapi import FastAPI


app = FastAPI()

app.include_router(router_user, prefix="/user")
app.include_router(router_course, prefix="/course")
