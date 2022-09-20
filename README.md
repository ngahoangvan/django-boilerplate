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
GET | `/users/list` | Get list users
GET | `/users/me` | Get current user
PUT/PATCH | `/users/me` | Update current user
GET | `/users/<user_id>` | Get user by id

## Installation
### Pre-requisite
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

### Extensions - Setup JupyterLab for Django Project

- Step 1: Install Jupyter Lab package
```bash
pip install jupyterlab
```

- Step 2: Use below config inside ```src/app/settings/dev.py```
```py
try:
    import jupyterlab
    notebook_default_url = '/lab'
except ImportError:
    notebook_default_url = '/tree'

NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0',
    '--port', '8888',
    '--NotebookApp.default_url', notebook_default_url,
]
IPYTHON_KERNEL_DISPLAY_NAME = 'Django Kernel'
```

- Step 3: Start Jupyter Lab server

```bash
python manage.py shell_plus --notebook
```

## Folder Structure
```bash
.
├── bin                          # folder of bash file as quick tool
│   └── gunicorn.sh
│   └── dc-*.sh                  # script for docker-compose
│
├── docker-compose.db.dev.yml    # docker-compose file for db
├── docker-compose.yaml          # docker-compose file for development
├── requirements                 # requirements folder
│   ├── all.txt
│   ├── common.txt
│   ├── dev.txt
│   ├── prod.txt
│   └── test.txt
└── src                          # django source app
    ├── app                      # core setting
    ├── authentication           # authentication app
    ├── users                    # user app
    ├── tests                    # unit test
    ├── manage.py                # django manage file
    └── ... 
```

## TODO list
- [x] DRF JWT Authentication
- [x] Get value from **.env** file
- [x] Users api CRUD endpoints
- [x] Add docker configurations
- [x] Document folder structure
- [x] Configure static/media & templates
- [x] Unit test
- [x] Setup Jupyter Lab 
- [ ] Integrate reactjs
- [ ] Github action
