from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import BlogArticel

from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    blogs = BlogArticel.objects.all();
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST["password"]
        user = authenticate(username=username,password=pwd)
        if user is not None:
            login(request,user)
            return render(request, "main.html", {'blogs':blogs, 'user':user})
    return render(request, "main.html", {'blogs':blogs, 'user':None})

def createBlog(request):
    newBlog = BlogArticel();
    newBlog.title = request.POST['title']
    newBlog.blog_content = request.POST['blog_content']
    newBlog.author = request.user
    newBlog.save()
    blogs = BlogArticel.objects.all();
    return render(request, "main.html", {'blogs':blogs, 'user':request.user})
