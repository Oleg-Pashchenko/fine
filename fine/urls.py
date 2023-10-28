from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:telegram_id>/', include('home.urls')),
    path('<int:telegram_id>/', include('finance.urls')),
    path('<int:telegram_id>/', include('notes.urls')),
    path('<int:telegram_id>/', include('targets.urls')),
    path('<int:telegram_id>/', include('tasks.urls'))
]
