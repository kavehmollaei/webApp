
from django.urls import path

from website.views import index
from blog.views import blog_single,blog_view



app_name='blog'


urlpatterns = [
path('',blog_view,name='index'),
path('<int:pid>',blog_single,name='blog_single'),

# path('details/',blog_details,name='blog_details')
]
