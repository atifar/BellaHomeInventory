# BHF Inventory


## Overview

BHF Inventory is an inventory and sales listing management website. It currently implements most of the inventory management functionality.

## Installation

Start a virtual environment with python 3 and Django v1.8. Clone the repository. Create a PostGres database, whose name you'll need to enter in the local_settings.py file in the Django project's configuration root (see example below). Create a Django admin superuser, and enter the username and password into local_settings.py. You may load initial database data for the website using the following command:

```
python3 manage.py loaddata bhf_dump.json
```

## Django local_settings.py Example

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': <database>,
        'USER': <username>,
        'PASSWORD': <password>,
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
