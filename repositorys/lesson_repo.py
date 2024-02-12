from fastapi import Response
from config.supabasedb import supabase_db


supabase_db = supabase_db()


class LessonRepository:
    def get_lesson_in_course_all(self, uid):
        try:
            get_lesson_in_course_all = (
                supabase_db.table("courseLessons")
                .select("*")
                .eq("course_uid", uid)
                .execute()
            )
            return get_lesson_in_course_all.data
        except Exception as e:
            return {"error": e}

    def get_lesson(self, uid):
        try:
            get_lesson = (
                supabase_db.table("courseLessons").select("*").eq("uid", uid).execute()
            )
            return get_lesson.data
        except Exception as e:
            return {"error": e}
