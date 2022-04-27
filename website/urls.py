from django.urls import path,re_path
from  website.views import about, http_test,json_response,index,contact,template,blog,service

app_name='website'

urlpatterns = [
# path('blog/',http_test),
path('blog/json/',json_response),
path('',index , name='index'),
path('about/' ,about,name='about'),
path('class/',service,name='service'),
path('blogfa/',blog,name='blog'),
# re_path(r'^[a-c]/',about),
path('contact/',contact),
path('template/',template),
path('contact',contact,name='contact'),
]
