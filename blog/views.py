from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Denis Kotlyarchuk',
        'title': 'My First Post',
        'content': "Yeah, I did it! My first post",
        'date_posted': "August 18, 2018"
    },
    {
        'author': 'John Doe',
        'title': 'Second Post',
        'content': "Second post content bruh",
        'date_posted': "August 19, 2018"
    },
]


def home(request):
    return render(request, 'blog/home.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')
