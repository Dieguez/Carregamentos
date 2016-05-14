from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.conf.urls import patterns
from django.contrib import admin
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello!")










