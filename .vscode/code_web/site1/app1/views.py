from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("You're at the polls index.")
def index1(request):
    return HttpResponse("Hello world.")
