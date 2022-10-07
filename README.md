# Django API Generator

The tool is able to `generate APIs` using **Django & DRF** stack with a minimum effort. For newcomers, **Django** is a leading backend framework used to code from simple websites and APIs to complex eCommerce solutions.

- 👉 Free [support](https://appseed.us/support/) via Email and [Discord](https://discord.gg/fZC6hup)
- 👉 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

<br />

## How It Works

> 👉 **Step #1** - Define models in `apps/models.py`

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

> 👉 **Step #2** - `Migrate Database`

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 **Step #3** - `Generate API` 

```bash
$ python manage.py generate-api
```

`Note`: if you define a model that wasn't migrated to db, you will see an error that say names of not migrated models and codes will not generate.

<br />

> 👉 **Step #4** - `Use the API` 

* Create a book by `POST` request to `/api/books/`
* Get book that has id = 2 by `GET` request to `/api/books/2/`
* Get all books by `GET` request to `/api/books/`
* Update book that has id = 2 by `PUT` request to `/api/books/2/`
* delete book that has id = 2 by `DELETE` request to `/api/books/2/`

<br />

> 👉 **Step #5** - API Authentication

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
