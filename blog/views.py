from datetime import date
import imp
from multiprocessing.spawn import import_main_path
from django.shortcuts import render
from datetime import date


# Create your views here.
def blog_view(request):
    content={'title':'why mathemathic??','author':'noora habibi','date_publish':date.today()}
    

    return render(request,'blog/blog.html',context=content)

def blog_single(request):
    return render(request,'blog/blog-item.html')

def test(request):
    return render(request,'blog/test.html')    