from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/all_blogs.html', context)

 