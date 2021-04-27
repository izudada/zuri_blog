# A Completed Zuri Internship Blog Task 

Features Include:

-    A register page, a user can perform CRUD operations both for creating articles and and read for comments. 

-    login.

-    reset password (Only on their Profile page when logged in.)

-    logout

-    A comment section (can only create for now)

-    Heroku Link at [here](https://izudada-blog.herokuapp.com/)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/zuri_blog.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install pipenv:

https://pypi.org/project/pipenv/

then to activate a virtual enviroment:

```sh
$ pipenv shell
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(folder_name)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `pipenv` using your folder or root directory name.

## Database

In source folder locate the settings.py file, change the database section or variable with the code below to create your local db.

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
The above will create a local db for you immediately you run django server.


Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Tests

To run the tests, `cd` into the directory or make sure you are in the same directory where `manage.py` is:
```sh
(folder_name)$ python manage.py test blog
```
