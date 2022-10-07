# Django API Generator

The tool is able to `generate APIs` using **Django & DRF** stack with a minimum effort. For newcomers, **Django** is a leading backend framework used to code from simple websites and APIs to complex eCommerce solutions.

- 👉 Free [support](https://appseed.us/support/) via Email and [Discord](https://discord.gg/fZC6hup)
- 👉 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

<br />

## How It Works

> 👉 **Step #1** - Define models in `apps/models.py`

By default, the project comes with a simple `Books` model: 

```python
class Book(models.Model):

    name = models.CharField(max_length=100)
```

<br />

> 👉 **Step #2** -  `Register the model` in `core/settings.py` (API_GENERATOR section)

```python
API_GENERATOR = {
    'books': "Book", # <-- Books model provided as sample
}
```

<br />

> 👉 **Step #3** - `Migrate Database`

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 **Step #4** - `Generate API` 

```bash
$ python manage.py generate-api
```

`Note`: if you define a model that wasn't migrated to db, you will see an error that say names of not migrated models and codes will not generate.

<br />

> 👉 **Step #5** - `Use the API` 

* Create a book by `POST` request to `/api/books/`
* Get book that has id = 2 by `GET` request to `/api/books/2/`
* Get all books by `GET` request to `/api/books/`
* Update book that has id = 2 by `PUT` request to `/api/books/2/`
* delete book that has id = 2 by `DELETE` request to `/api/books/2/`

<br />

> 👉 **Step #6** - API Authentication

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

<br />

--- 
**Django API Generator** - Developer tool provided by [AppSeed](https://appseed.us)
