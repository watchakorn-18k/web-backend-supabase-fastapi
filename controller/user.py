from fastapi import APIRouter, Depends, HTTPException, Request, Response
from middleware.check_user import check_cookie_login
from models.user_model import EmailModel, NewPasswordModel, UserModel
from repositorys.user_repo import UserRepository
from services.user_service import UserService


router_user = APIRouter()
router = router_user

user_service = UserService(UserRepository())


@router.get("/")
async def index():
    return {"status": "ok", "data": "Hello World"}


@router.get("/profile")
async def profile(response=Depends(check_cookie_login)):
    return response


@router.post("/signup")
async def signup(user: UserModel):
    data_sign_up = user_service.sign_up(user)
    return {"status": "ok", "data": data_sign_up}


@router.post("/signin")
async def signin(user: UserModel, response: Response):
    data_sign_in = user_service.sign_in(user, response)
    return {"status": "ok", "data": data_sign_in}


@router.get("/confirm{token}")
async def confirm(token: str, response: Response):
    values = dict(item.split("=") for item in token.split("#")[1].split("&"))
    response.set_cookie(key="access_token", value=values["access_token"], httponly=True)
    response.set_cookie(key="type", value=values["type"], httponly=True)
    return values


@router.post("/chang-new-password")
async def chang_new_password(new_password: NewPasswordModel, response: Response):
    data_chang_new_password = user_service.chang_new_password(
        new_password.validate(), response
    )
    return data_chang_new_password


@router.get("/logout")
async def logout():
    data_logout = user_service.sign_out()
    return data_logout


@router.post("/reset-password")
async def reset_password(email: EmailModel):
    data_reset = user_service.reset_password(email)
    return data_reset
