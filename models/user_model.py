from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    password: str
    model_config = {"email": "test@test.com", "password": "12345678"}


class EmailModel(BaseModel):
    email: str
    model_config = {"email": "test@test.com"}


class NewPasswordModel(BaseModel):
    new_password: str
    confirm_password: str

    model_config = {"new_password": "12345678", "confirm_password": "12345678"}

    def validate(self):
        if self.new_password != self.confirm_password:
            return {"status": "fail", "data": "password not match"}
        else:
            return {"status": "ok", "data": NewPasswordModel(**self.dict())}
