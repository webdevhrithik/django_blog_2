from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 17, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 10, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogapp/home.html', context)

def about(request):
    return HttpResponse('<h1>About Page</h1>')