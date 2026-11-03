from flask import render_template, request, redirect, url_for, flash

from app.models.task import MovieModel


class MovieController:
    def __init__(self):
        self.model = MovieModel()

    def index(self):
        movies = self.model.get_all_movies()
        return render_template('movies/index.html', movies=movies)

    def store(self):
        title = request.form.get('title', '').strip()
        if not title:
            flash('Назва не може бути порожньою!', 'error')
            return redirect(url_for('index'))

        try:
            year = int(request.form.get('year', 0) or 0)
            duration = int(request.form.get('duration', 0) or 0)
        except ValueError:
            flash('Рік і тривалість мають бути числами!', 'error')
            return redirect(url_for('index'))

        added = self.model.add_movie(
            genre=request.form.get('genre', '').strip() or "None",
            title=title,
            director=request.form.get('director', '').strip() or "B",
            year=year,
            duration=duration,
            studio=request.form.get('studio', '').strip() or "idk",
            name=request.form.get('actor_name', '').strip() or "idk",
            role=request.form.get('actor_role', '').strip() or "looser",
        )

        if added:
            flash('Фільм додано!', 'success')
        else:
            flash('Такий фільм уже є у списку', 'error')

        return redirect(url_for('index'))

    def mark_watched(self, movie_id: int):
        if self.model.mark_watched(movie_id):
            flash('Фільм позначено як переглянутий!', 'success')
        else:
            flash('Фільм не знайдено', 'error')
        return redirect(url_for('index'))

    def delete(self, movie_id: int):
        if self.model.delete_movie(movie_id):
            flash('Фільм видалено!', 'success')
        else:
            flash('Фільм не знайдено', 'error')
        return redirect(url_for('index'))