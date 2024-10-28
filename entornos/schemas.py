from pydantic import BaseModel

class UserSchema(BaseModel):

    name: str
    last_name: str 
    email: str
    phone: str

class MovieSchema(BaseModel):

    name: str
    release_year: int
    duration: str
    director: str
    rating: str
    genre: str