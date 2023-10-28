from django.shortcuts import render
from django.http import HttpRequest


def main(request: HttpRequest):
    return render(request, 'core/main.html', {'disable_navbar': True})


def my_day(request: HttpRequest, telegram_id: int):
    return render(request, 'app/home/my-day.html')

