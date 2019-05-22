# Django GraphQL Trial

Application to test out using GraphQL in Django.

Built with Python3.

## Requirements

- Python 3.7
- Django 2.2

## Installation

### Clone Project

```sh
git clone https://github.com/taiyeoguns/django-graphql-trial.git
```

### Get Pipenv

If not already installed, [install Pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)

### Install Requirements

Create virtual environment and install the application requirements:

```sh
pipenv install
```

Thereafter activate environment by running:

```sh
pipenv shell
```

To deactivate environment, run:

```sh
exit
```

### Add details in `.env` file

Create `.env` file from example file and maintain necessary details in it.

```sh
cp .env.example .env
```

### Run migrations

Create tables in the database:

```sh
python manage.py migrate
```

### Seed database

To populate database with sample data, run:

```sh
python manage.py seed
```

### Run the application

Start the application by running:

```sh
python manage.py runserver
```

Open a browser and navigate to `http://localhost:8000/graphql`

### Sample Request

In Graphiql, enter the following sample request:

```
query {
  departments {
    uuid
    name
    createdAt
  }
}
```

### Tests

In command prompt, run:

```sh
pytest -v
```

### Further Information

- [https://medium.com/@alhajee2009/graphql-with-django-a-tutorial-that-works-2812be163a26](https://medium.com/@alhajee2009/graphql-with-django-a-tutorial-that-works-2812be163a26)
- [https://gearheart.io/blog/how-to-use-graphql-with-django-with-example/](https://gearheart.io/blog/how-to-use-graphql-with-django-with-example/)
- [https://www.howtographql.com/graphql-python/2-queries/](https://www.howtographql.com/graphql-python/2-queries/)
