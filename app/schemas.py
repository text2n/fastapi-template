from pydantic import BaseModel

class Hero(BaseModel):
    id: int
    name: str
    age: int
    secret_name: str