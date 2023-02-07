from django.urls import path
from . import views

app_name = 'tema'
urlpatterns = [
    path('', views.course1, name='course1'),
]