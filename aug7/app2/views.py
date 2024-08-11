from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def func1(request):
    return render(request,'home.html')

def func2(request):
    if request.user.is_authenticated:
        messages.warning(request,"Mama you already logged! ")
        return redirect('homepage')
    #logout(request)
    if request.method=="POST":
        a=request.POST.get('uname')
        b=request.POST.get('passw')
        result=authenticate(request,username=a,password=b)
        if result is not None:
            #print(a,b,type(result))
            login(request,result)
            messages.success(request,"Thank you for coming back ! ")
            return redirect('profilepage')
        else:
            messages.error(request,"are you trying to cheat me ! Wrong creds")
           
    return render(request,'login.html')




@login_required(login_url='LoginPage')
def func4(request):
    if request.user.is_superuser:
        print(request.user.username)
        return redirect('/admin')
    return render(request,'profile.html')

def func5(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        passw=request.POST.get('passw')
        cpass=request.POST.get('cpass')
        mail=request.POST.get('mail')
        print(fname,lname,passw,cpass,mail,uname)
        if User.objects.filter(username=uname).exists():
            messages.error(request,"Username already exists !")
            return redirect('loginpage')
        if len(passw)<8:
            messages.error(request,"Password must be 8 chars")
            return redirect('registerpage')
        #validation for cpass
        if (cpass!=passw):
            messages.error(request,"Passwords doest match")
            return redirect('registerpage')
        
        obj=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=mail,password=passw)
        obj.save()
        messages.success(request,"Hey your account is ready, Login now")
        return redirect('loginpage')

    return render(request,'register.html')

def func6(request):
    return render(request,'single.html')

@login_required(login_url='LoginPage')
def func7(request):
    return render(request,'create.html')


def logoutV(request):
    logout(request)
    messages.info(request,"are you there bro")
    return redirect('loginpage')