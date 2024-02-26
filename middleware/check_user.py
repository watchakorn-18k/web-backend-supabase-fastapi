from fastapi import Request, Response

from config.supabasedb import supabase_db


supabase_db = supabase_db()


def check_cookie_login(request: Request, response: Response) -> Response:
    token_user = request.headers.get("Authorization").replace("Bearer ", "")
    # token_in_db = ""
    print(token_user)
    if token_user:
        try:
            if supabase_db.auth.get_user(token_user):
                return supabase_db.auth.get_user()
        except Exception as e:
            return {"status": "fail", "data": e}
        # token_in_db = supabase_db.auth.get_user(token_user).dict().get("id")
        # if token_in_db:
        #     return {"status": "ok", "data": token_in_db}

    return {"status": "fail", "data": "Please login"}
