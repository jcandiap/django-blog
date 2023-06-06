from django.shortcuts import render, HttpResponse

# Create your views here.
app_name = 'user'

def profile(request):
    return HttpResponse('test')