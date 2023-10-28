from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect

import home.views


class IsTelegramAccountIdValidMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.path != '/':
            telegram_id = request.path.split('/')[1]
            if not telegram_id.isdigit():
                messages.warning(request, "Указан некорретный адрес! Перенаправляю на главную.")
                return redirect(home.views.main)
            telegram_id = int(telegram_id)
            # TODO: check telegram id
        response = self.get_response(request)
        return response
