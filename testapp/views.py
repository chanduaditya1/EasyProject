from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    s='<Html><header><h1>HELLO WORLD OF DJANGO</H1></header></html>'
    return HttpResponse(s)
