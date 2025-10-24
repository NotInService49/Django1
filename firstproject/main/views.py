from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1> Web Development with Ike! <!h1>")

def v1(reponse):
    return HttpResponse("<h> View 1! <!h>")