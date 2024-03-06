from django.urls import path
from .views import homePageView
from .views import home

urlpatterns = [
    path("", homePageView, name="home"),
    path("/home/", home, name="home1")
]
