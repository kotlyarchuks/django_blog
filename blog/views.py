from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView


def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all()})

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    return render(request, 'blog/about.html')
