from django.contrib import admin

# Register your models here.
from .models import About, Post

admin.site.register(About)
admin.site.register(Post)
