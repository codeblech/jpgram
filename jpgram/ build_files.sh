curl -sSL https://install.python-poetry.org | python3 -
poetry install
poetry run python manage.py collectstatic --noinput

