# [Django API Generator](https://appseed.us/developer-tools/django-api-generator/)

The tool is able to `generate APIs` using **Django & DRF** stack with a minimum effort. For newcomers, **Django** is a leading backend framework used to code from simple websites and APIs to complex eCommerce solutions.

- 👉 Free [support](https://appseed.us/support/) via Email and [Discord](https://discord.gg/fZC6hup)
- 👉 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

<br />

## Quick start in `Docker`

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/devtool-django-api-generator.git
$ cd devtool-django-api-generator
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. By default a simple [Books](./apps/models.py) Model is used as sample.  

- The generated DRF API is live at `http://localhost:5085/api/books`
- Registered users can interact with the API using the `API-View` page

<br />

![Django API Generator - API View page for Books Model.](https://user-images.githubusercontent.com/51070104/194476781-6476de62-191a-48e8-8730-344c2d63f9d0.png) 

<br />

## Video Presentation

https://user-images.githubusercontent.com/51070104/194480046-fe920d98-e3ac-4c65-9e70-8b752ffaff05.mp4

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
**[Django API Generator](https://appseed.us/developer-tools/django-api-generator/)** - Developer tool provided by [AppSeed](https://appseed.us)
