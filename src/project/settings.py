import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJ_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    "rest_framework.authtoken",
    "djoser",
    "polls",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# ==============================================================

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# ==============================================================

STATIC_URL = "/static/"

# ????????????????????? static???????????????????????????
STATICFILES_DIRS = [BASE_DIR / "static"]

# collect ?????????????????????????????????
STATIC_ROOT = str(BASE_DIR / "public/static/")

# media files (?????????????????????????????????????????????????????????????????????)
# ==============================================================
MEDIA_ROOT = os.path.join(BASE_DIR, "site_media/")
MEDIA_URL = "/media/"

# other django default settings
# ==============================================================

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS
# ==============================================================
CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True

# REST framework
# ==============================================================
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # page base
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # offset base
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
}

# spectacular (API document)
# https://drf-spectacular.readthedocs.io/en/latest/settings.html
# ==============================================================
SPECTACULAR_SETTINGS = {
    "SERVE_PERMISSIONS": [
        "rest_framework.permissions.AllowAny" if DEBUG else "rest_framework.permissions.IsAdminUser"
    ],
    "SWAGGER_UI_SETTINGS": {
        "persistAuthorization": True,
    },
    # request, response ??? ??????????????????????????????. frontend ??????????????? create ???????????????(POST) ????????? readonly field ???????????????????????????
    "COMPONENT_SPLIT_REQUEST": True,
    # /api/ ??? prefix ?????????
    # TODO: ??????????????????????????? swagger ??? ?????????????????? URL ??? /api/ ??????????????? 404 ?????????????????????
    #       ??????????????????????????????????????????????????????????????? env ???????????????????????????????????????????????? swagger url ??????????????????????????????
    "SCHEMA_PATH_PREFIX_TRIM": "/api/" if os.getenv("ENABLE_SCHEMA_PATH_PREFIX_TRIM", "0") == "1" else "",
}

# email
# ==============================================================
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# djoser
# https://djoser.readthedocs.io/en/latest/
# ==============================================================
DJOSER = {"SEND_ACTIVATION_EMAIL": True, "ACTIVATION_URL": "http://example.com/activate/{uid}/{token}"}
