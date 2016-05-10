from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.conf.urls import patterns
from django.contrib import admin
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def my_view(request):
    return HttpResponse("Hello!")


def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns('',
            (r'^my_view/$', admin.site.admin_view(my_view))
        )
        return my_urls + urls
    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls



