# Django-DRF Boilerplate

This boilerplate to create a simple Django project with django rest framework


## List endpoints
#### Authentication token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/auth/register` | Register new user
POST | `/auth/login` | Login
POST | `/auth/token/refresh` | Refresh token
POST | `/auth/logout` | Logout

#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/auth/users` | Get list users

## Installation
### Pre-require
- Python 3.8+
- PIP

### Create your python virtual environment
Some virtualenv you can follow. Currently, I'm using miniconda.

- With conda/miniconda
```bash
$ conda create -n venv python=3.8
$ conda activate venv
```

- With virtualenv
```bash
# Install virtualenv from pip
$ pip install virtualenv

# create 
$ python -m venv venv
$ source .venv/bin/active
```

- With pipenv
```bash
# Install pipenv from pip
$ pip install --user pipenv
```

After create your python virtual environment and activate it, the console
will look like:
```bash
(venv) $
```

### Install and running project

```bash
# Clone the project
(venv) $ git clone https://github.com/ngahoangvan/django-boilerplate.git
# Go to project
(venv) $ cd django-boilerplate
# Install package
(venv) $ pip install requirements.txt
# Copy .env file
(venv) $ cp src/.env.example src/.env
# Create migration
(venv) $ python src/manage.py makemigrations 
# Apply migration file
(venv) $ python src/manage.py migrate
# Run server
(venv) $ python src/manage.py run server
```

**Note**: If you got issue is connection with database, please look at 
```src/app/settings/common.py``` to edit DATABASES setting


## TODO list
- [x] DRF JWT Authentication
- [x] Get value from **.env** file
- [ ] Users api CRUD endpoints
- [ ] Add docker configurations
- [ ] Document folder structure
- [ ] Configure Static/media & templates
- [ ] Unit test
- [ ] Integrate reactjs
- [ ] Github action
