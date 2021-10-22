from django.urls import path
from .models import *
from . import views


urlpatterns = [
    path("", views.index,name="home"),
    path("add", views.add,name="add")
]


