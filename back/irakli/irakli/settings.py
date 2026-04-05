import os
from pathlib import Path

# BASE_DIR ახლა არის: .../iraklis film/back/irakli
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ds)-lka57h8o)&#46^sj@m$e2=wn277-i=9fn30_wniv)o^kur'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'owner', # შენი აპლიკაციის სახელი (თუ owner დაარქვი)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'irakli.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ავდივართ 2 საფეხურით ზემოთ, რომ მივწვდეთ front-ს
        'DIRS': [BASE_DIR.parent.parent / 'front'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'irakli.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'ka-ge'
TIME_ZONE = 'Asia/Tbilisi'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

# აქაც ავდივართ 2 საფეხურით ზემოთ CSS-ისთვის და სურათებისთვის
STATICFILES_DIRS = [
    BASE_DIR.parent.parent / 'front',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'