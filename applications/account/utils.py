from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Py29',
        f'Привет перейди по этой ссылке чтобы активировать аккаунт: \n\n http://localhost:8000/api/account/activate/{code}',
        'RodionDereha@gmail.com',
        [email]
    )

def send_activate(email, code):
    send_mail(
        'Уведомление о смене пароля',
        'Ваш пароль был успешно изменен.',
        'RodionDereha@gmail.com',
        [email],
        fail_silently=False,
    )