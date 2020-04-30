from django.http import HttpResponse
from django.db import models
from rest_framework import viewsets
from blog.serializers import PostSerializer
from blog.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
