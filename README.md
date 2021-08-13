# Simple Polynomial Evaluator

`Important note`: .env file is published for demo purposes only to ease application setup.

## Tech
Rest API use a number of open source projects to work properly:

- [Flask] - Lightweight web application framework.
- [Flask-Migrate] - Flask extension that handles SQLAlchemy database migrations using Alembic.
- [Flask-RESTful] - Flask extension that adds support for quickly building REST APIs. 
- [Flask-SQLAlchemy] - Flask extension that adds support for SQLAlchemy to your application.
- [marshmallow] - ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes
- [pytest] - Testing framework.
- [webargs] - Python library for parsing and validating HTTP request objects.
- [python-dotenv] - Python-dotenv reads key-value pairs from a .env file and can set them as environment variables.
## Installation
### Installation using Docker

The easiest way to install, navigate to the project root and type in your preferred terminal:
```sh
$ docker-compose up
```

Verify the installation by navigating to link below in your preferred browser.

```sh
http://127.0.0.1:8000/
```


## Testing

Before testing, make sure container is running and you installed application successfully.

### Testing using Docker

Navigate to the project root and type in your preferred terminal:
```sh
$ docker-compose exec web bash
coverage run -m pytest
```


[Flask]: https://flask.palletsprojects.com/
[Flask-Bcrypt]: https://flask-bcrypt.readthedocs.io/en/latest/
[Flask-Migrate]: https://flask-migrate.readthedocs.io/en/latest/
[Flask-RESTful]: https://flask-restful.readthedocs.io/en/latest/
[Flask-SQLAlchemy]: https://flask-sqlalchemy.palletsprojects.com/
[marshmallow]: https://marshmallow.readthedocs.io/en/stable/
[PyJWT]: https://pyjwt.readthedocs.io/en/stable/
[pytest]: https://pytest.org
[python-dotenv]: https://pypi.org/project/python-dotenv/
[webargs]: https://webargs.readthedocs.io/en/latest/
