from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_email(to, subject, template, **kwargs):
    # Get the application context so we can get environment variables from it.
    app = current_app._get_current_object()
    # Construct the message.
    msg = Message(subject, sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    # Send the email.
    with app.app_context():
        mail.send_message(msg)
