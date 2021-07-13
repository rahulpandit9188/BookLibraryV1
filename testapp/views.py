from django.shortcuts import render
from django.http import HttpResponse


def greeting(request):
    s = "<h1>Good Morning</h1>"
    return HttpResponse(s)


def about(request):
    s = "<h1>Good Night rahul</h1>"
    return HttpResponse(s)


def contect(request):
    s = "<h1>ajitpanditkuttanumber1</h1>"
    return HttpResponse(s)
