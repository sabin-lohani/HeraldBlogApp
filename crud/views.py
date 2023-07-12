from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, "crud/index.html")
def about(req):
    return render(req, "crud/about.html")