
from django.urls import path

from website.views import index
from blog.views import blog_single,blog_view,test,blog_details



app_name='blog'


urlpatterns = [
path('',blog_view,name='index'),
path('blog/single',blog_single,name='single'),
path('<str:name>/<str:family_name>',test,name='test'),
path('details/',blog_details,name='blog_details')
]
