from django.urls import path

from . import views

app_name = "course"

urlpatterns = [
    path("낙산", views.home1, name = "낙산"),
    path("남산", views.home2, name = "남산"),
    path("백악", views.home3, name = "백악"),
    path("숭례문", views.home4, name = "숭례문"),
    path("인왕산", views.home5, name = "인왕산"),
    path("흥인지문", views.home6, name = "흥인지문"),
]
