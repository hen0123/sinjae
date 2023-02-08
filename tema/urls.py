from django.urls import path
from . import views

app_name = 'tema'
urlpatterns = [
    path('tema1/', views.tema1, name='tema1'),
    path('tema2/', views.tema2, name='tema2'),
    path('tema3/', views.tema3, name='tema3'),
    path('tema4/', views.tema4, name='tema4'),

]