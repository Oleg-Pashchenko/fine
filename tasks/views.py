from django.shortcuts import render
from django.http import HttpRequest


def edit(request: HttpRequest, telegram_id: int):
    return render(request, 'app/targets/edit.html')


def list_page(request: HttpRequest, telegram_id: int):
    return render(request, 'app/targets/list.html')


