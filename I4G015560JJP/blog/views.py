from msilib.schema import ListView
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy

from I4G015560JJP.blog.models import Post

from django.views.generic.list import CreateView
from django.views.generic.list import UpdateView
from django.views.generic.list import DeleteView

# Create your views here.

class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostUpdateView(UpdateView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")