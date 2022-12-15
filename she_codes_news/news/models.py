from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, 
        related_name='posts',
    )
    pub_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    image_url = models.URLField(blank=True)
    # favourites = models.ManyToManyField(get_user_model(), related_name='favourite', default=None, blank=True)

    
