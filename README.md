
## Django Northwind

Django Northwind is a version of the Microsoft Northwind sample database.

The Northwind database is an excellent tutorial schema for a
small-business ERP, with categories, customers, region, territories,
employees, shippers, suppliers, products and orders.

### Practice with different schemas like SqLite, MySql, Postgres or
others using Django Northwind.

## Files

* Diagram:
    * northwind/diagram/northwind_diagram.png
* Data:
    * Postgres sql script
    * Sample data for django
        * northwind/fixtures/northwind.json

## How to use

### Choose the folder that you are going to use
```bash
cd codes
```

### Python

Install the dependencies required by the Python environment.
For ubuntu:

```bash
sudo apt-get install python-dev python-pip
```

### Create the virtualenv. Remember to use python 3

```bash
virtualenv northwind_db
```

### Clone Repository

```bash
git clone << Repository Url>>
```

### Change the working directory to the repository
```bash
cd django_project
```

### Install requirements. Remember to activate the virtual environment.
```bash
pip install -r requirements.txt
```

### Runserver
Use the runserver to execute the application:

```bash
python manage.py runserver
```

### After choosing the database in settings.py
create the schemas for the databases
```bash
python manage.py migrate
```

### Populate the database with the sample data
```bash
python manage.py loaddata northwind/fixtures/northwind.json
```

### Notes for Postgres

For Postgres you need to install psycopg2:
```bash
pip install psycopg2==2.7.5
```

Enter to postgres shell

Create user for Postgres
```bash
CREATE ROLE 'DATABASE_NAME' WITH LOGIN ENCRYPTED PASSWORD 'DATABASE_PASSWORD';
```

Create database for Postgres
```bash
CREATE DATABASE 'DATABASE_NAME' WITH OWNER = DATABASE_NAME;
```

Sample configuration for Postgres settings database
```bash
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}
```
