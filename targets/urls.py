from django.urls import path

from targets import views

urlpatterns = [
    path('edit/', views.edit, name='edit'),
    path('list/', views.list_page, name='list')
]
