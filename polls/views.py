from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("lets create the polls ")
# Create your views here.
