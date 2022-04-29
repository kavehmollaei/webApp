from email.mime import image
from ssl import create_default_context
from statistics import mode
from tabnanny import verbose
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
    class Meta:
        ordering= ['created_date']
        verbose_name = 'postBlog'
        verbose_name_plural = 'postBlog'  




    def __str__(self) -> str:
        return f"{self.id}-{self.title}"
    



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  

    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name