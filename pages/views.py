from django.shortcuts import render

from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, World!")


def home(request):
    return HttpResponse("ghdjgjgfdjkdhg")


# Create your views here.
