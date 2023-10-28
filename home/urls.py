from django.urls import path

from home import views

urlpatterns = [
    path('my-day/', views.my_day, name='my_day')
]
