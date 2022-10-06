# Django API Generator

The tool is able to generate APIs using Flask, Flask-RestX stack with a minimum effort. For newcomers, Flask is a leading backend framework used to code from simple websites and APIs to complex eCommerce solutions.

- 👉 Free [support](https://appseed.us/support/) via Email and [Discord](https://discord.gg/fZC6hup)
- 👉 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

<br />

## Video Presentation

https://user-images.githubusercontent.com/51070104/194334755-b5cc63d7-4b64-45b5-bf8e-da92d73bc4ba.mp4

<br />

## How It Works

> Step #1 - Define models in `apps/models.py`

<br />

> Register the model in `core/settings.py` with this pattern:

```python
API_GENERATOR = {
    'endpoint': 'ModelName',
    'books': "Book",
    'cities': "City",
}
```

<br />

> Migrate Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Generate API 

```bash
$ python manage.py generate-api
```

`Note`: if you define a model that wasn't migrated to db, you will see an error that say names of not migrated models and codes will not generate.

<br />

> Use the API 

* Create a book by `POST` request to `/api/books/`
* Get book that has id = 2 by `GET` request to `/api/books/2/`
* Get all books by `GET` request to `/api/books/`
* Update book that has id = 2 by `PUT` request to `/api/books/2/`
* delete book that has id = 2 by `DELETE` request to `/api/books/2/`

<br />

> API Authentication

There are 2 models of authentication that you can use.

> **Token Based Authentication**: send post request to `/login/jwt/` with username and password in body. Api will return a token.

```
POST /login/jwt/ {
    "username": "sth",
    "password": "sth"
}
```

The token should be used in all mutating requests (Create, Update, Delete)

```
{
  "Authorization": "token {your token}"
}
```

Example:

```
{
  "Authorization": "token b36705e1078b4b67d4dc4f1388a1aee4a754d4cd"
}
```

<br />

> **Basic Authentication** 

For users authenticated in the app. 

--- 
**Django API Generator** - Developer tool provided by [AppSeed](https://appseed.us)
