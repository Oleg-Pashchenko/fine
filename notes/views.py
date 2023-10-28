from django.shortcuts import render
from django.http import HttpRequest


def edit(request: HttpRequest, telegram_id: int):
    return render(request, 'app/notes/edit.html')


def list_page(request: HttpRequest, telegram_id: int):
    return render(request, 'app/notes/list.html')


def view(request: HttpRequest, telegram_id: int):
    return render(request, 'app/notes/view.html')

