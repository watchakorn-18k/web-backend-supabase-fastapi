from controller.user import router_user
from controller.course import router_course
from controller.lesson import router_lesson
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="web-backend-supabase-fastapi")

origins = ["http://localhost", "http://localhost:3000", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_user, prefix="/api/user")
app.include_router(router_course, prefix="/api/course")
app.include_router(router_lesson, prefix="/api/course/lesson")
