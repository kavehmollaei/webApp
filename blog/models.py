
import re
from django.db import models
from django.contrib.auth.models import User





#Cathegory Model
class Category(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name
  
        


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=100000000)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    #tags
    category =models.ManyToManyField(Category)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    counted_views = models.IntegerField(default=0) #defaulr=0
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        ordering= ['created_date']
        verbose_name = 'postBlog'
        verbose_name_plural = 'postBlog'  


    def count_posts_of(user):
        return Post.objects.filter(author=user).count()

    def __str__(self) -> str:
        return f"{self.id}-{self.title}"

    def snippets(self):
        return self.content[:100] + '...'  
   
   
    



# craete Contact model
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


class UserProfile(models.Model):
    address = models.CharField(max_length=255,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    about = models.TextField(max_length=500,blank=True)     
