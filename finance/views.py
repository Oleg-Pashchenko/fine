from django.shortcuts import render
from django.http import HttpRequest


def predictions(request: HttpRequest, telegram_id: int):
    return render(request, 'app/finance/predictions.html')


def review(request: HttpRequest, telegram_id: int):
    return render(request, 'app/finance/review.html')


