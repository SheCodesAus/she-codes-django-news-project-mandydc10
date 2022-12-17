from django.contrib import admin
# from .models import NewsStory
from . import models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')

admin.site.register(models.NewsStory, AuthorAdmin)