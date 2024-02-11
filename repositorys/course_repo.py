from fastapi import Response
from config.supabasedb import supabase_db
from models.course_model import Course


supabase_db = supabase_db()


class CourseRepository:
    def get_last_id(self):
        try:
            get_last_id, _ = (
                supabase_db.table("courses").select("id").order("id").execute()
            )
            return get_last_id[-1][-1]["id"]

        except Exception as e:
            return "error", e

    def get_course_all(self):
        try:
            get_course_all, _ = supabase_db.table("courses").select("*").execute()
            # print(get_course_all[1], type(get_course_all[1]))
            return get_course_all[1]
        except Exception as e:
            return "error", e

    def add_course(self, course):
        try:
            course.id = self.get_last_id() + 1
            add_course = supabase_db.table("courses").insert(course.dict()).execute()
            return add_course
        except Exception as e:
            return "error", e

    def edit_course(self, course):
        try:
            edit_course = (
                supabase_db.table("courses")
                .update(course.dict())
                .eq("id", course.id)
                .execute()
            )
            return edit_course
        except Exception as e:
            return "error", e

    def get_course(self, id):
        try:
            get_course = supabase_db.table("courses").select("*").eq("id", id).execute()
            return get_course.dict()["data"]
        except Exception as e:
            return "error", e

    def delete_course(self, id):
        try:
            delete_course = supabase_db.table("courses").delete().eq("id", id).execute()
            return delete_course.dict()["data"]
        except Exception as e:
            return "error", e
