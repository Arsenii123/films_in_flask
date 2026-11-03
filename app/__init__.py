from flask import Flask
from app.controllers.task_controller import MovieController

def create_app():
    app = Flask(__name__, template_folder='views/templates')
    app.secret_key = 'super-secret-key-for-flash' # Flask зберігає flash-повідомлення
    # не в базі даних і не в пам'яті сервера, а в cookie браузера користувача (в сесії).
    # cесія в Flask — це підписаний (signed) словник, який зберігається в cookie.
    # підпис робиться за допомогою секретного ключа (secret_key).
    # без секретного ключа Flask не може створити безпечну сесію, а значить не може зберегти flash-повідомлення

    # екземпляр контролера
    controller = MovieController()

    # реєстрація маршрутів та їх обробників
    @app.route('/', methods=['GET'])
    def index():
        return controller.index()

    @app.route('/store', methods=['POST'])
    def store():
        return controller.store()

    @app.route('/watched/<int:movie_id>', methods=['POST'])
    def mark_watched(movie_id):
        return controller.mark_watched(movie_id)

    @app.route('/delete/<int:movie_id>', methods=['POST'])
    def delete(movie_id):
        return controller.delete(movie_id)

    return app