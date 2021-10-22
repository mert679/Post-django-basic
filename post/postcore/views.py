from django.shortcuts import render,redirect
from django.conf import settings
from .models import Post
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.

def index(request):
    allpost= Post.objects.all()
    context = {
        "all": allpost,
        
    }
    return render(request,"posts/index.html",context)

def add(request):
   
    
    if request.method == "POST" :
     
        title = request.POST["title"]
        description = request.POST["description"]
    
        addpost = Post(title=title,description=description)
        addpost.save()
        return redirect("/")
       
        
    
    return render(request,"posts/add.html")