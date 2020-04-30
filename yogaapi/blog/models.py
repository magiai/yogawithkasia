from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    description = models.CharField(max_length=500)
    content = models.TextField()
    photo = models.ImageField(upload_to='blog_photos')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural  = "Posts"
        ordering = ['-created_on']

    def __str__(self):
        return self.title