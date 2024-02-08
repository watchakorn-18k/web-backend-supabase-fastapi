from fastapi import Response
from config.supabasedb import supabase_db


supabase_db = supabase_db()


class UserRepository:
    def sign_up_user(self, user):
        try:
            user_new = supabase_db.auth.sign_up(
                {"email": user.email, "password": user.password}
            )
            return user_new
        except Exception as e:
            return e

    def sign_in_user(self, user):
        try:
            user_sign = supabase_db.auth.sign_in_with_password(
                {"email": user.email, "password": user.password}
            )
            return user_sign
        except Exception as e:
            return e

    def sign_out(self):
        try:
            user_sign = supabase_db.auth.sign_out()
            return user_sign
        except Exception as e:
            return e

    def reset_password(self, email):
        try:
            user_reset = supabase_db.auth.reset_password_email(email.email)
            return user_reset
        except Exception as e:
            return e

    def chang_new_password(self, passwords: dict, response: Response):
        try:
            passwords_new = supabase_db.auth.update_user(
                {"password": "portonbad1234"},
            )

            return passwords_new
        except Exception as e:
            return e
