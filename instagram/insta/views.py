from django.shortcuts import render
from insta.models import *

# Create your views here.
def func1(request):
    a=POST.objects.all()
    if request.method=="POST":
        b=request.POST.get('search')
        result=POST.objects.filter(caption_contains=b)
        return render(request,'index.html',{'res':result})
    return render(request,'index.html',{'res':a})

def func2(request):
    if request.method=="POST":
        image=request.FILES.get('img')
        capt=request.POST.get('cap')
        obj=POST(users=request.user,photo=image,caption=capt)
        obj.save()
    return render(request,'feed.html')