# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uhr0amz$9%2&ow4j#o+xo)&ki7@tunhlwpruurn+s$x*%u($f^'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bhf_inventory',
        'USER': 'ati',
        'PASSWORD': 'v3l0c!t!',
        'HOST': 'localhost',
        'PORT': '',
    }
}
