from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ok(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def docker_try(request):
    return HttpResponse("Hello, world. from docker.")
