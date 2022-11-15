# LilyTech

### A single vendor ecommerce app API


This project is the API of LilyTech, a single ecommerce app.

To run this project locally on Linux based systems and MacOs:

You must have python 3.6 higher versions installed

- clone the project: `git clone git@github.com:milkiyd/lilytech_api.git`
- navigate to the project directory: `cd lilytech_api`
- create a virtual environment: `python3 -m venv venv`
- activate the environment: `source venv/bin/activate`
- install dependencies: `pip install -r requirements.txt`
- create database and tables: `./manage.py makemigrations store && ./manage.py migrate`
- start the server: `./manage.py runserver`
- navigate to 127.0.0.1:{port_number}/api

In order to add items to database
- create a super user: `./manage.py createsuperuser` and follow instructions
- navigate to 127.0.0.1:{port_number}/admin
- add your data to database
- navigate back to 127.0.0.1:{port_number}/api/ to see the what you entered
