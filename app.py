from http import HTTPStatus
from main import create_app
from werkzeug.utils import redirect

app = create_app()


@app.route('/')
def index():
    return redirect('/swagger-ui'), HTTPStatus.PERMANENT_REDIRECT


if __name__ == '__main__':
    app.run()
