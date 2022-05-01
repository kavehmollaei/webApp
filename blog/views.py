from datetime import date
import imp
from multiprocessing.spawn import import_main_path
import re
from django.shortcuts import render
from datetime import date
from blog.models import Post

# Create your views here.
def blog_view(request):
    # content={'title':'why mathemathic??','author':'noora habibi','date_publish':date.today()}
    posts=Post.objects.filter(status=True)
    content={"posts": posts}
    return render(request,'blog/blog.html',context=content)

def blog_single(request):

    return render(request,'blog/blog-item.html')

def test(request,name,family_name):
    
    content={"firstname":name,"lastname":family_name}
    return render(request,'blog/test.html',context=content) 


def blog_details(request):
    return render(request,'blog/blog-item.html')