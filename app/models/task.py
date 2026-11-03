from dataclasses import dataclass
from typing import List


@dataclass
class Actor:
    name: str
    role: str


@dataclass
class Movie:
    id: int
    genre: str
    title: str
    director: str
    year: int
    duration: int
    studio: str
    actor: Actor
    watched: bool = False


class MovieModel:
    def __init__(self):
        self._movies: List[Movie] = []
        self._next_id = 1

    def add_movie(self, genre="None", title="A", director="B", year=0,
                  duration=0, studio="idk", name="idk", role="looser") -> bool:
        # дубликат: тот же фильм с тем же годом
        for m in self._movies:
            if m.title.lower() == title.lower() and m.year == year:
                return False
        movie = Movie(self._next_id, genre, title, director, year,
                      duration, studio, Actor(name, role))
        self._movies.append(movie)
        self._next_id += 1
        return True

    def get_all_movies(self) -> List[Movie]:
        return self._movies.copy()

    def mark_watched(self, movie_id: int) -> bool:
        for movie in self._movies:
            if movie.id == movie_id:
                movie.watched = True
                return True
        return False

    def delete_movie(self, movie_id: int) -> bool:
        before = len(self._movies)
        self._movies = [m for m in self._movies if m.id != movie_id]
        return len(self._movies) < before