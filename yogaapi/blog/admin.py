from django.contrib import admin
from django.contrib.admin import register

# Register your models here.
from blog.models import Post

@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']