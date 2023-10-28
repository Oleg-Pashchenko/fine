from django.urls import path

from finance import views

urlpatterns = [
    path('predictions/', views.predictions, name='predictions'),
    path('review/', views.review, name='review')
]
