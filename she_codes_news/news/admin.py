from django.contrib import admin
# from .models import NewsStory
from . import models

class AuthorAdmin(admin.ModelAdmin):
    display_list = ('title', 'author')

admin.site.register(models.NewsStory, AuthorAdmin)