# API challenge

### How to run:

- git clone https://github.com/matousidc/api_challenge.git
- (create and activate venv)
- pip install -r requirements.txt
- python manage.py runserver

### Comments:

- used python 3.11
- root url redirected to /countries/
- country_code max length is 3
- group_id set as null, left for updating with PUT
- id - set up as auto-increment
- versioned also DB for easier set up