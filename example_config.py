DB_FILENAME = '<sqlite filename goes here>'
# http://docs.celeryproject.org/en/latest/configuration.html
BROKER_URL = 'redis://localhost/1'

CELERY_IMPORTS = [
    'cliche.crawler'
]
