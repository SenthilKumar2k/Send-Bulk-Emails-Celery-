pip install celery redis


# settings.py

# Application definition

INSTALLED_APPS = [

    # 'channels',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'celery',
]

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0' # Example using Redis as broker
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0' # Example using Redis as result backend
#CELERY_ACCEPT_CONTENT = [‘application/json’]
#CELERY_TASK_SERIALIZER = config(‘CELERY_TASK_SERIALIZER’, ‘’)
#CELERY_RESULT_SERIALIZER = config(‘CELERY_RESULT_SERIALIZER’, ‘’)
#CELERY_TIMEZONE = config(‘CELERY_TIMEZONE’, ‘’)

# Email Backend Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Example using SMTP as email backend
EMAIL_HOST = 'your_smtp_host'
EMAIL_PORT = 587  # or the appropriate port for your SMTP server
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
EMAIL_USE_TLS = True  # Set it to True if your SMTP server requires TLS/SSL
#EMAIL_USE_SSL=FALSE
#SENDER_EMAIL=""


