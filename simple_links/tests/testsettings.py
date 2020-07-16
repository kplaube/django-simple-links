from typing import List

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
SECRET_KEY = "dsl"
INSTALLED_APPS = ['simple_links']
MIDDLEWARE_CLASSES: List[str] = []
