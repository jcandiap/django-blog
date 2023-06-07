from django.shortcuts import render, HttpResponse

# Create your views here.
app_name = 'blog'

def index(request):
    return render(request, 'blog/index.html')