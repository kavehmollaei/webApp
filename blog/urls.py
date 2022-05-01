
from django.urls import path

from website.views import index
from blog.views import blog_single,blog_view



app_name='blog'


urlpatterns = [
path('',blog_view,name='index'),
path('blog/single',blog_single,name='single'),
path('<int:pid>',blog_single,name='blog_single'),

]
