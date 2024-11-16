from django.urls import path

from . import views

app_name = "gestao"

urlpatterns = [
    path("", views.index, name="index")
]
