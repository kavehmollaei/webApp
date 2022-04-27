from email.mime import image
from ssl import create_default_context
from statistics import mode
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    #image
    #tags
    #category
    #author
    counted_views = models.IntegerField(default=0) #defaulr=0
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.id}-{self.title}"




