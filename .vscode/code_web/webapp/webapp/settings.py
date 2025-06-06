"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 5.0.12.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
from  dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api
import logging

logger = logging.getLogger('allauth')
logger.setLevel(logging.DEBUG)

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['4e3f-14-226-121-70.ngrok-free.app', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'accounts',
    'rest_framework',
    'rest_framework_simplejwt',
    "django_extensions",
    'cloudinary',
    'cloudinary_storage',
    
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '925757706340-srn97tn9fffv21g6sto1uisidf4vaa4o.apps.googleusercontent.com',
            'secret': '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',
        },
        'AUTH_PARAMS': {
            'access_type': 'online',
            'prompt': 'select_account'
        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': True
    },
    'github': {
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        }
    }
}
# 
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
ACCOUNT_LOGIN_METHODS = {"username", "email"}
ACCOUNT_EMAIL_VERIFICATION = "none" 
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_LOGIN_ON_GET = True  
ACCOUNT_LOGOUT_ON_GET = True
SITE_ID = 1
SOCIALACCOUNT_ADAPTER = 'accounts.adapters.MySocialAccountAdapter'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
}

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # Token sống trong 5 phút
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # Refresh token sống 7 ngày
#     'ROTATE_REFRESH_TOKENS': True,  # 🔥 Tự động cấp refresh token mới
#     'BLACKLIST_AFTER_ROTATION': True,  # 🔥 Token cũ sẽ bị vô hiệu hóa
# }

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dmjxgbywe',
    'API_KEY': os.getenv('API_KEY'),
    'API_SECRET': os.getenv('API_SECRET'),
}
cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE["CLOUD_NAME"],
    api_key=CLOUDINARY_STORAGE["API_KEY"],
    api_secret=CLOUDINARY_STORAGE["API_SECRET"],
)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware', 
    'django.middleware.common.CommonMiddleware',     
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware', 
]


ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'accounts/templates'],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.getenv('DB_NAME'),        # Tên database bạn đã tạo
        'HOST': os.getenv('DB_HOST'),      # Nếu SQL Server chạy trên máy
        'PORT': os.getenv('DB_PORT'),           # Port mặc định của SQL Server
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # Kiểm tra driver đang dùng
        },
        'USER': os.getenv('DB_USER'),    # Thay 'your_username' bằng tên đăng nhập SQL của bạn
        'PASSWORD': os.getenv('DB_PASSWORD'),  # Thay 'your_password' bằng mật khẩu của bạn
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SESSION_COOKIE_SECURE = False  
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = "sessionid"
SESSION_SAVE_EVERY_REQUEST = True

#smtp
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.getenv('Email_Google')    
EMAIL_HOST_PASSWORD = os.getenv('Pass_Google')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER            
