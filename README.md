# Django URL Shortener
A simple URL shortener built with Django. This project allows users to shorten long URLs into manageable, shareable links.
-----------------------------------------------------------------------------------------
## Features
Shorten long URLs into compact, unique short codes.

Redirect users from the short URL to the original URL.

Simple and user-friendly interface.
-----------------------------------------------------------------------------------------
### Technologies Used
Backend: Django

Database: SQLite (default) 

Frontend: HTML, CSS, JavaScript 
-----------------------------------------------------------------------------------------
### Installation
Follow these steps to set up the project locally.
Prerequisites
Python 3.8 or higher
pip (Python package manager)
-----------------------------------------------------------------------------------------
```sh
  git clone https://github.com/NeduStack/python-url-shortner.git
  cd python-url-shortner
```
-----------------------------------------------------------------------------------------
### Set up a virtual environment:
```sh
  python -m venv venv
  source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```
-----------------------------------------------------------------------------------------
### Install dependencies:
```sh
  pip install -r requirements.txt
```
-----------------------------------------------------------------------------------------
### Run migrations:
```sh
  python manage.py migrate
```
-----------------------------------------------------------------------------------------
### Create a superuser (optional):
```sh
  python manage.py createsuperuser
```
-----------------------------------------------------------------------------------------
### Run the development server:
```sh
  python manage.py runserver
```
