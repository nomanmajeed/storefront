from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage

from store.tasks import notify_customers


def draft_mail(request):
    try:
       message = BaseEmailMessage(
           template_name='emails/email_template.html',
           context={'name': 'Noman Majeed'}
       )
       message.send(['hammad@admin.com'])
    except BadHeaderError:
        pass
    return render(request, 'emails/email_template.html', {'name': 'Noman Majeed'})


def test_celery(request):
    notify_customers.delay('Hello')
    return render(request, 'test.html', {'name': 'Noman'})