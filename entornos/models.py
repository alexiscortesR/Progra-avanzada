from sqlmodel import SQLModel, Field

class MoviesModel(SQLModel, table=True):
    __tablename__ = "movies"

    id: int = Field(primary_key=True)
    name: str
    release_year: int
    duration: str
    director: str
    rating: str
    genre: str
    