# DSMS
Django School Management System With Student Staff Login and Sign Up Dashboards 

## Setup

The first thing to do is to download the repository:

install the dependencies:

```sh
$ pip install pipenv

```

after installing pipenv create virtual env via pipenv
```sh
$ pipenv shell
```
this will create and active virtual env 

then run `pipenv lock` this will download tools and libraries used in this project 

Once `pipenv lock` has finished downloading the dependencies:

then check `settings.py` for database setup i used sqlite,

then run migrations,
```sh
$ python manage.py makemigrations
```
```sh
$ python manage.py migrate
```
once the migrations finished then run,
```sh
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`

login as admin:
email:xbwafi@gmail.com
password: khan

login as Staff:
`http://127.0.0.1:8000/`
email:javed@mail.com
password: password

login as Student:
`http://127.0.0.1:8000/`
email:student@gmail.com
password: password



for any error or problem contact me,
email: xbwafi@gmail.com
whatsapp:0093788730001
