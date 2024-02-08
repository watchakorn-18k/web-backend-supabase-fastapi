from fastapi import Request, Response
from models.user_model import EmailModel, UserModel
from repositorys.user_repo import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def sign_up(self, user: UserModel):
        data_user = self.user_repository.sign_up_user(user)
        return data_user

    def sign_in(self, user: UserModel, response: Response):
        data_user = self.user_repository.sign_in_user(user)

        if len(dir(data_user)) > 50:
            response.set_cookie(
                key="access_token", value=data_user.session.access_token, httponly=True
            )
        return data_user

    def sign_out(self):
        data_logout = self.user_repository.sign_out()
        if data_logout is None:
            return {"status": "ok", "data": "Sign out successfully"}
        return data_logout

    def reset_password(self, email: EmailModel):
        data_reset = self.user_repository.reset_password(email)
        return data_reset

    def chang_new_password(self, passwords: dict, response: Response):
        data_chang_new_password = self.user_repository.chang_new_password(
            passwords, response
        )
        response.delete_cookie("type")

        return data_chang_new_password
