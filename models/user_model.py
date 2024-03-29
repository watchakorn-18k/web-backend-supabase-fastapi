from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    password: str


class EmailModel(BaseModel):
    email: str


class NewPasswordModel(BaseModel):
    new_password: str
    confirm_password: str

    def validate(self):
        if self.new_password != self.confirm_password:
            return {"status": "fail", "data": "password not match"}
        else:
            return {"status": "ok", "data": NewPasswordModel(**self.dict())}
