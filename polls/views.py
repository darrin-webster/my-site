from django.shortcuts import render

from django.http import HttpResponse

#gives hello world page when url is called
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")