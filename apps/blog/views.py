from django.shortcuts import render, HttpResponse

# Create your views here.
app_name = 'blog'

def index(request):
    return HttpResponse('XD')