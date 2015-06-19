from __future__ import absolute_import

from celery import shared_task
from messcover import actions


@shared_task
def run_spider():
    actions.run_spider()
