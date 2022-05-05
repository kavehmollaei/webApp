from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag
def hello():
    return 'Hello'

@register.simple_tag(name="totalposts")
def function():
    posts = Post.objects.filter(status=1).count()
    return posts



@register.simple_tag(name='posts')
def function():
    post=Post.objects.filter(status=1)
    return post
 

@register.filter(name='snippet')
def snippet(value:str,arg=20):
    return value[:arg] + '...'


@register.inclusion_tag('blog/recentpost.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:2]
    return {'posts':posts}
