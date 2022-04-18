from __future__ import absolute_import, unicode_literals

import logging
import os

from celery import Celery

logger = logging.getLogger("Celery")

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    # Só pra debug
    print('Request: {0!r}'.format(self.request))
