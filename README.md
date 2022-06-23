## Description

Events online is an application that allow user to see events and can also add events
## Features

User can login and see events according to category

## View Live Site here

https://celevents.herokuapp.com/

## Technologies Used

- Python 3.8
- Django MVC framework
- HTML, CSS and Bootstrap
- JavaScript
- Postgressql
- Heroku
## Prerequisite

The events-online project requires a prerequisite understanding of the following:

Django Framework
Python3.8
Postgres
Python virtualenv

## Setup and installation

# Clone the Repo from

https://github.com/chepceline/events.git

# Activate virtual environment

Activate virtual environment using python3.6 as default handler virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate

# Install dependancies

Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

# Create the Database

- psql
- CREATE DATABASE insta;
# .env file

Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = '<DB_name'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

# Run initial Migration

python3.8 manage.py makemigrations 
python3.8 manage.py migrate

# Run the app

python3.8 manage.py runserver
Open terminal on localhost:8000
# knownbugs
Some images could no load

# Contributors
- Damaris Chepchirchir

# Contact Information
chepceline25@gmail.com