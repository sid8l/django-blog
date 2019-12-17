from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, index page posts')


def detail(request, post_id):
    response = f'Here you can see full post about {post_id}'
    return HttpResponse(response)
