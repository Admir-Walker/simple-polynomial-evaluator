from http import HTTPStatus
from flask_migrate import Migrate
from main import create_app
from werkzeug.utils import redirect

from main import db

app = create_app()
migrate = Migrate(app, db)


@app.route('/')
def index():
    return redirect('/swagger-ui'), HTTPStatus.PERMANENT_REDIRECT


if __name__ == '__main__':
    app.run()
