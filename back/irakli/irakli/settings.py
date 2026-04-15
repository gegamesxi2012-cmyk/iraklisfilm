import os
from pathlib import Path

# BASE_DIR არის შენი 'back' ფოლდერი
BASE_DIR = Path(__file__).resolve().parent.parent

# უსაფრთხოების გასაღები
SECRET_KEY = 'django-insecure-ds)-lka57h8o)&#46^sj@m$e2=wn277-i=9fn30_wniv)o^kur'

# დეველოპმენტის დროს True, ჩაბარებისას თუ სერვერზე გაუშვებ - False
DEBUG = True

# ყველასთვის ხელმისაწვდომი რომ იყოს
ALLOWED_HOSTS = ['*']

# აპლიკაციები
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'owner', # დარწმუნდი, რომ შენს აპლიკაციას ზუსტად ეს ჰქვია
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
        # აი, აქ დაემატა მეორე .parent, რომ 'back'-იდან სრულად გამოვიდეს
        'DIRS': [os.path.join(BASE_DIR.parent.parent, 'front')], 
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

# მონაცემთა ბაზა (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# პაროლის ვალიდაცია (სტანდარტული)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ენა და დრო
LANGUAGE_CODE = 'ka' # ქართული ენა
TIME_ZONE = 'Asia/Tbilisi'
USE_I18N = True
USE_TZ = True

# სტატიკური ფაილები (CSS, JS, Images)
STATIC_URL = 'static/'

# მივუთითებთ სად ეძებოს CSS ფაილები
# settings.py-ში იპოვე STATICFILES_DIRS და ასე ჩაწერე:
STATICFILES_DIRS = [
    os.path.join(BASE_DIR.parent.parent, 'front', 'static'),
]

# მედია ფაილების ადგილი (თუ ფილმების პოსტერებს ტვირთავ)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR.parent, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'