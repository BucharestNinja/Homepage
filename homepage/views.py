from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic import DetailView
from django.utils import timezone
# Create your views here.

class PostIndex(ListView):
    model = Post
    paginate_by = 7
    template_name='homepage/blog.html'

class PostDetailView(DetailView):
    model = Post
    template_name='homepage/post_detail.html'

def home(request):
    return render(request,'homepage/home.html',{})

def team(request):
    return render(request,'homepage/team.html',{})

def contact(request):
    return render(request,'homepage/contact.html',{})

def products(request):
    return render(request,'homepage/products.html',{})
