from django.shortcuts import render
from app1.models import *
# Create your views here.
def home(request):
    results=Book.objects.all()
    return render(request,'home.html',{Book:results})

def createAuthor(request):
    if request.method=="POST":
        name=request.POST.get('aname')
        age=request.POST.get('age')
        rating=request.POST.get('rat')
        print(name,age,rating)
        obj=Author(name=name,age=age,rating=rating)
        obj.save()
    return render(request,'author.html')

def createBook(request):
    if request.method=="POST":
        t=request.POST.get('aname')
        p=request.POST.get('price')
        g=request.POST.get('gener')
        s=request.POST.get('author')
        a=Author.objects.get(id=s)
        obj=Book(title=t,price=p,gener=g,author=a)
        obj.save()
    return render(request,'book.html')