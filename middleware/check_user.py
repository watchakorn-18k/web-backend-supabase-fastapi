from fastapi import Request, Response

from config.supabasedb import supabase_db


supabase_db = supabase_db()


def check_cookie_login(request: Request, response: Response) -> Response:
    token_user = request.cookies.get("access_token")
    token_in_db = ""
    if token_user:
        token_in_db = supabase_db.auth.get_session()
        if token_in_db:
            return {"status": "ok", "data": token_in_db}

    if token_user == token_in_db:
        return supabase_db.auth.get_user()
    return {"status": "fail", "data": "Please login"}
