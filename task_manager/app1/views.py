from django.shortcuts import render,redirect
from .forms import RegisteruserForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def homepage(request):
    return render(request,'home.html')

def RegisterUser(request):
    if request.method == 'POST':
        form = RegisteruserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Login_page)
    else:
        form = RegisteruserForm()
    return render(request,'register.html',{'form':form})

def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect(homepage)
        
    return render(request,'login.html')
