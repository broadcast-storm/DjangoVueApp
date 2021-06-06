"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key")
# REFRESH_TOKEN_SECRET = env("REFRESH_TOKEN_SECRET",
#                            default="unsafe-refresh-secret-key")

ACCESS_TOKEN_EXPIRES = env("ACCESS_TOKEN_EXPIRES", default=5)
REFRESH_TOKEN_EXPIRES = env("REFRESH_TOKEN_EXPIRES", default=14)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
# DEBUG = True

ALLOWED_HOSTS = ['yandex-gamification.std-884.ist.mospolytech.ru', '127.0.0.1']

# Application definition

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

INSTALLED_APPS = [
    'baton',
    'django_crontab',
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'api.apps.ApiConfig',
    'taggit',
    'django_cleanup',
    'easy_thumbnails',

     'baton.autodiscover', #at the end
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://127.0.0.1:8080',
)


# CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

AUTH_USER_MODEL = 'api.UserProfile'

TAGGIT_CASE_INSENSITIVE = True

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none',
    'SECURITY_DEFINITIONS': {
        'USE_SESSION_AUTH': False,
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # make all endpoints private
    )
}

CRONJOBS = [
    ('* 23 * * *', 'django.core.management.call_command',
     ['flushexpiredtokens'])
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Vue project location
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

# Vue assets directory (assetsDir)
STATICFILES_DIRS = [
    os.path.join(FRONTEND_DIR, 'dist/static'),
]


# Webpack output location containing Vue index.html file (outputDir)
TEMPLATES[0]['DIRS'] += [
    os.path.join(FRONTEND_DIR, 'dist'),
]

SIMPLE_JWT = {
    'SIGNING_KEY': SECRET_KEY,
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=ACCESS_TOKEN_EXPIRES),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=REFRESH_TOKEN_EXPIRES),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}


LOGGING = {
    'version': 1,
    'loggers': {
        'django': {
            'handlers': ['fileDebug', 'fileInfo'],
            'level': 'DEBUG'
        }
    },
    'handlers': {
        'fileDebug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './logs/debug.log',
            'formatter': 'UsualFormat'
        },
        'fileInfo': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': './logs/info.log',
            'formatter': 'UsualFormat'
        }
    },
    'formatters': {
        'UsualFormat': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{'
        }
    }
}

THUMBNAILS_ALIASES = {
    '': {
        'default': {
            'size': (96, 96),
            'crop': 'scale',
        },
    },
}

THUMBNAILS_BASEDIR = 'thumbnails'

BATON = {
    'SITE_HEADER': 'Геймификация',
    'SITE_TITLE': 'ЮMoney.Геймификация',
    'INDEX_TITLE': 'Панель администратора',
    'SUPPORT_HREF': 'https://github.com/nikita220800/DjangoVueApp',
    'COPYRIGHT': 'Copyright © 2021 <a href="//mospolytech.ru" target="_blank">MosPolytech</a>',
    'POWERED_BY': '<a href="//mospolytech.ru" target="_blank">MosPolytech</a>',
    'MENU_TITLE': 'Меню',
    'GRAVATAR_DEFAULT_IMG': 'mp',
    'LOGIN_SPLASH': '/frontend/src/assets/img/auth/background.jpg',

    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    # 'CHANGELIST_FILTERS_FORM': False,
    # 'MENU_ALWAYS_COLLAPSED': True,

    'MENU': (
        { 'type': 'title', 'label': 'Задания', 'apps': ('api', ) },
        { 'type': 'model', 'label': 'Квест', 'name': 'mainquest', 'app': 'api' },
        { 'type': 'model', 'label': 'Задачи', 'name': 'task', 'app': 'api' },
        { 'type': 'model', 'label': 'Тесты', 'name': 'test', 'app': 'api' },

        { 'type': 'title', 'label': 'Поощрения', 'apps': ('api', ) },
        { 'type': 'model', 'label': 'Ачивки', 'name': 'achievement', 'app': 'api' },
        { 'type': 'model', 'label': 'Товары', 'name': 'product', 'app': 'api' },

        { 'type': 'title', 'label': 'Пользователи', 'apps': ('api', ) },
        { 'type': 'model', 'label': 'Подразделения', 'name': 'division', 'app': 'api' },
        { 'type': 'model', 'label': 'Команды', 'name': 'team', 'app': 'api' },
        { 'type': 'model', 'label': 'Сотрудники', 'name': 'userprofile', 'app': 'api' },
    ),

    # example of Google Analytics
    # 'ANALYTICS': {
    #     'CREDENTIALS': os.path.join(BASE_DIR, 'credentials.json'),
    #     'VIEW_ID': '12345678',
    # },
}
