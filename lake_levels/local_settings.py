DEBUG = True 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'teps5lnk6z%y#x(x&w&3p^3_!_lbx(n!8a4cjuk_+qhg!9%_5@'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lake_levels',
        'HOST': 'localhost',
        'USER': 'marcuspeterson',
        'PASSWORD': '',
        'PORT': '5432',
    }
}