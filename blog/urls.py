
from django.urls import path

from website.views import index
from blog.views import blog_single,blog_view,test



app_name='blog'


urlpatterns = [
path('',blog_view,name='index'),
path('blog/single',blog_single,name='single'),
path('post-<int:pid>',test,name='test'),
]
