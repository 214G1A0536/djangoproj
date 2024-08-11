from django.shortcuts import render
from Hotel.models import Menu
def home(request):
    result=Menu.objects.all()
    if request.method=='Post':
        sno=int(request.POST.get('sno'))
        if Menu.objects.filter(id=sno).exists():
            abc=Menu.objects.get(id=sno)
        else:
            abc=None
        return render(request,'home.html',{"res":result,'res2':abc})
    return render(request,'home.html',{'res':result})
def add(request):
    result=Menu.objects.all()
    if request.method=='POST':
        a=str(request.POST.get('name'))
        b=str(request.POST.get('type'))
        obj=Menu(name=a,type=b)
        obj.save()
        return render(request,'home.html')
    return render(request,'home.html',result)
# Create your views here.