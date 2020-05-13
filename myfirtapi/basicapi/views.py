from django.shortcuts import render
import requests
from rest_framework import viewsets
from .serializers import Postserializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = Postserializer

# Create your views here.

def home(request):
    response=requests.get("http://127.0.0.1:8000/posts/")
    data=response.json()
    return render(request,'home.html',{'data':data})