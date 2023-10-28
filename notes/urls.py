from django.urls import path

from notes import views

urlpatterns = [
    path('edit/', views.edit, name='edit'),
    path('list/', views.list_page, name='list'),
    path('view/', views.view, name='view')
]
