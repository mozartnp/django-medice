import time

from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

logger = get_task_logger(__name__)


@shared_task
def print_numbers(max_number):
    logger.info('Creating the task...')

    _sec = 3
    logger.info('Wait {} seg'.format(_sec))
    time.sleep(_sec)
    for i in range(max_number):
        logger.info(i)

    logger.info('Finishing task...')
    return True


@shared_task
def my_send_mail(subject, message, from_email, to):
    '''
    Envia email via Celery.
    '''
    send_mail(subject, message, from_email, to)


@shared_task
def send_mail_to_user_via_celery(domain, use_https, user_email, user_pk, token, from_email, to):  # noqa E501
    # Não aceita request.
    subject = 'Ative sua conta.'
    message = render_to_string('email/account_activation_email.html', {
        'user': user_email,
        'protocol': 'https' if use_https else 'http',
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(user_pk)),
        'token': token,
    })
    send_mail(subject, message, from_email, to)
