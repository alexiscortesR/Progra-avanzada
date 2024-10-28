from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from user import UserModel
from random import randint
from sqlmodel import select
from schemas import UserSchema
from schemas import MovieSchema
from models import MoviesModel

app = FastAPI()
create_db_and_tables()

@app.post("/users")
async def create_user(database:SessionDep, user_data: UserSchema):

    user = UserModel(name = user_data.name, last_name = user_data.last_name, email=user_data.email, phone = user_data.phone)
    database.add(user)
    database.commit()
    database.refresh(user)
    return user

@app.get ("/users")
async def get_users(database: SessionDep):
    statement = select(UserModel)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get ("/users/{user_id}")
async def get_user_by_id(user_id: int, database: SessionDep):
    user = database.get(UserModel, user_id)
    if not user:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Usuario no encontrado")
    return user


@app.post("/movies")
async def create_movie(movie_data: MovieSchema, database: SessionDep):
    movie = MoviesModel(
        name = movie_data.name,
        release_year = movie_data.release_year,
        duration = movie_data.duration,
        director = movie_data.director,
        rating= movie_data.rating,
        genre = movie_data.genre
    )

    database.add(movie)
    database.commit()
    database.refresh(movie)

    return movie

@app.get("/movies")
async def get_movies(database: SessionDep):
    statement=select(MoviesModel)
    results=database.exec(statement)
    items=results.all()
    return items

@app.get("/movies/{movie_id}")
async def get_movie_by_id(movie_id: int, database: SessionDep):
    movie=database.get(MoviesModel, movie_id)

    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pelicula no encontrada"
        )
    
    return movie