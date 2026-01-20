from pathlib import Path
import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ==================================================
# LOAD ENV
# ==================================================
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# ==================================================
# SECURITY
# ==================================================
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# ==================================================
# APPLICATIONS
# ==================================================
INSTALLED_APPS = [

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',

    # Project apps
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'store.apps.StoreConfig',
    'orders.apps.OrdersConfig',
]

# ==================================================
# MIDDLEWARE
# ==================================================
MIDDLEWARE = [

    # 🔥 WhiteNoise (أساسي لحل مشكلة admin)
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==================================================
# URL CONFIG
# ==================================================
ROOT_URLCONF = 'mashailm.urls'

# ==================================================
# TEMPLATES
# ==================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# ==================================================
# WSGI
# ==================================================
WSGI_APPLICATION = 'mashailm.wsgi.application'

# ==================================================
# DATABASE
# ==================================================
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("DEV_DB_ENGINE"),
            'NAME': BASE_DIR / os.getenv("DEV_DB_NAME"),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("PROD_DB_ENGINE"),
            'NAME': os.getenv("PROD_DB_NAME"),
            'USER': os.getenv("PROD_DB_USER"),
            'PASSWORD': os.getenv("PROD_DB_PASSWORD"),
            'HOST': os.getenv("PROD_DB_HOST"),
            'PORT': os.getenv("PROD_DB_PORT"),
            'CONN_MAX_AGE': 600,
        }
    }

# ==================================================
# PASSWORD VALIDATION
# ==================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==================================================
# LANGUAGE & TIME
# ==================================================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# ==================================================
# STATIC FILES (WhiteNoise)
# ==================================================
STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# مهم جدًا للإنتاج
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ==================================================
# CLOUDINARY
# ==================================================
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media/'

# ==================================================
# DEFAULT PRIMARY KEY
# ==================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==================================================
# CUSTOM USER MODEL
# ==================================================
AUTH_USER_MODEL = 'accounts.User'
