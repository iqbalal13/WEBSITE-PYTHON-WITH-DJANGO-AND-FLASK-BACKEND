from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>IQBAL WEB PAGE")

def v1(response):
    return HttpResponse("<h1>HOME")