"""
Django settings for dashboard project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f5zs*!8)$-8y_a_6orw2rr6wk5@4&07mywmscw^lsgk*qs!+6p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_dashboard',
    'widget_tweaks',
    'ckeditor',
    'ckeditor_uploader',
    'whitenoise.runserver_nostatic', 
    'import_export' 
   
]

CKEDITOR_CONFIGS={
   'default': {
        # Toolbar configuration
         'toolbar':'full',
        # name - Toolbar name
        # items - The buttons enabled in the toolbar
        'toolbar_DefaultToolbarConfig': [
            {
                'name': 'basicstyles',
                'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                          'Superscript', ],
            },
            {
                'name': 'clipboard',
                'items': ['Undo', 'Redo', ],
            },
            {
                'name': 'paragraph',
                'items': ['NumberedList', 'BulletedList', 'Outdent', 'Indent',
                          'HorizontalRule', 'JustifyLeft', 'JustifyCenter',
                          'JustifyRight', 'JustifyBlock', ],
            },
            {
                'name': 'format',
                'items': ['Format', ],
            },
            {
                'name': 'extra',
                'items': ['Link', 'Unlink', 'Blockquote', 'Image', 'Table',
                          'CodeSnippet', 'Mathjax', 'Embed', ],
            },
            {
                'name': 'source',
                'items': ['Maximize', 'Source', ],
            },
        ],

        # This hides the default title provided by CKEditor
        'title': False,

        # Use this toolbar
        'toolbar': 'DefaultToolbarConfig',

        # Which tags to allow in format tab
        'format_tags': 'p;h1;h2',

        # Remove these dialog tabs (semicolon separated dialog:tab)
        'removeDialogTabs': ';'.join([
            'image:advanced',
            'image:Link',
            'link:upload',
            'table:advanced',
            'tableProperties:advanced',
        ]),
        'linkShowTargetTab': False,
        'linkShowAdvancedTab': False,

        # CKEditor height and width settings
        'height': '250px',
        'width': 'auto',
        'forcePasteAsPlainText ': True,

        # Class used inside span to render mathematical formulae using latex
        'mathJaxClass': 'mathjax-latex',

        # Mathjax library link to be used to render mathematical formulae
        'mathJaxLib': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_SVG',

        # Tab = 4 spaces inside the editor
        'tabSpaces': 4,

        # Extra plugins to be used in the editor
        'extraPlugins': ','.join([
            # 'devtools',  # Shows a tooltip in dialog boxes for developers
            'mathjax',  # Used to render mathematical formulae
            'codesnippet',  # Used to add code snippets
            'image2',  # Loads new and better image dialog
            'embed',  # Used for embedding media (YouTube/Slideshare etc)
            'tableresize',  # Used to allow resizing of columns in tables
        ]),
    },
    'special':{
        'toolbar':'Special',
        'toolbar_Special':[
            ['Bold','CodeSnippet']
        ],
        'extraPlugins':'codesnippet'
    }
}
CKEDITOR_UPLOAD_PATH='uploads/'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dashboard.urls'

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

WSGI_APPLICATION = 'dashboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIR=[
    os.path.join(BASE_DIR,'static')
]
MEDIA_URL = "/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"static/media/")
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CSRF_TRUSTED_ORIGINS=['https://*grants.up.railway.app/']
