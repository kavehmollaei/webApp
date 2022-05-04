from datetime import date
from email.mime import audio
from gc import get_objects
import imp
from multiprocessing.spawn import import_main_path
import re
from django.shortcuts import get_object_or_404, render
from datetime import date
from blog.models import Post,UserProfile,User,Category

# Create your views here.
def blog_view(request):
    # content={'title':'why mathemathic??','author':'noora habibi','date_publish':date.today()}
    category=Category.objects.all()
    
    #get len of category list
    lst=[]
    for item in category:
        lst.append(item)
    len_lst_category= len(lst)   
        
    posts=Post.objects.filter(status=True)
    content={"posts": posts,'category':category,'category_count':len_lst_category}
    return render(request,'blog/blog.html',context=content)

def blog_single(request,pid):
    
    post=get_object_or_404(Post,id=pid,status=True)
    category=Category.objects.all()
    
    userprofile=UserProfile.objects.all()
    content={'post':post,'userprofile':userprofile,'category':category}
    return render(request,'blog/blog-item.html',context=content)

def test(request,name,family_name):
    
    content={"firstname":name,"lastname":family_name}
    return render(request,'blog/test.html',context=content) 

