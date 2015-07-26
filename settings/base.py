import os

ALLOWED_HOSTS = []

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONTENT_TYPES = ['image', 'video']

DEBUG = True

INSTALLED_APPS = (
    'www',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


LANGUAGE_CODE = 'it'

MAX_UPLOAD_SIZE = "5242880"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'printers.urls'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

SUIT_CONFIG = {
    'ADMIN_NAME': 'Printerscout',
    'HEADER_DATE_FORMAT': 'l j F Y',
    'HEADER_TIME_FORMAT': 'H:i',
    'LIST_PER_PAGE': 500,
    'MENU': (
        'sites',
        {'app': 'auth', 'label': 'Utenti e gruppi', 'icon':'icon-lock', 'models': ('user', 'group')},
        {'app': 'www', 'icon': 'icon-print', 'models': ('www.printer', 'www.brand', 'www.company')},
    ),
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
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

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True

WSGI_APPLICATION = 'printers.wsgi.application'
