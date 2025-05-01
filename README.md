# School System

This is a small school system that allows us to look through and edit information about students, teachers, subjects, and classes. Registered users can **add**, **edit**, and **delete** data using special forms. 
Written with Django and Python. 

## Features

* View info of students, teachers, subjects, and classes
* Add new objects from the list shown above
* Edit existing information
* Delete objects
* User Registration
* Login system

## User Roles 

* Average User: has access only to Home page 
* Registered User: has access to viewing, adding, editing and deleting information


## Getting Started

First clone the repository from Github and switch to the new directory:

```bash
git clone https://github.com/dasha2020/test_django.git
cd test_django
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

Then just run the project: 

```bash

python manage.py runserver
```

Then go to this page in browser -> http://127.0.0.1:8000