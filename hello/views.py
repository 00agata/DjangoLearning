from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Post

def index(request):
    return HttpResponse("<marquee>Hello, world. You're at the polls index.</marquee>")


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
