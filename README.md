# A Completed Zuri Internship Blog Task 

Features Include:

-    A register page, a user can perform CRUD operations both for creating articles and and read for comments. 

-    login.

-    reset password (Only on their Profile page when logged in.)

-    logout

-    A comment section (can only create for now)

-    Heroku Link

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
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `pipenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd source
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Walkthrough

Before you interact with the application, go to GoCardless Sandbox and set up
the Redirect URI in the Developer settings. To make it work with this
application, use the value `http://127.0.0.1:8000/gocardless/confirm/`. This is to
make sure you are redirected back to your site where the purchase is verified
after you have made a purchase.


## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
# (env)$ python manage.py test gc_app
```
