from django.shortcuts import render
# Create your views here.
import re
from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse("kavehmollaei")

def json_response(request):
    return JsonResponse({'name':'kaveh'})

def about(request):
    return render(request,'website/about.html')    

def blog(request):
    return render(request,'blog/blog.html')


def index(request):
    return render(request,'website/index.html')


def contact(request):
    return render(request,'website/contact.html')

def service(request):
    return render(request,'website/service.html')

def template(request):
    template_tag={"name":"kavehmollaei"}
    return render(request,'website/index.html',context=template_tag)

