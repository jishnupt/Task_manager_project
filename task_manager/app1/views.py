from django.shortcuts import render,redirect
from .forms import RegisteruserForm,TaskAddForm
from django.contrib.auth import authenticate,login,logout
from .models import Task
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

def AdminRegist(request):
    if request.method == 'POST':
        form = RegisteruserForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.role = 'admin'
            return redirect(Login_page)
    else:
        form = RegisteruserForm()
    return render(request,'admin_reg.html',{'form':form})

def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if user.role == 'admin':
                return redirect(admin_dashbord)
            if user.role == 'user':
                return redirect(user_dashbord)    
    return render(request,'login.html')

def admin_dashbord(request):
    return render(request,'admin_page.html')

def user_dashbord(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request,'user_page.html',{'tasks':tasks})

def Logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect(homepage)
    else:
        return render(request,'logout.html')
    
def TaskAdding(request):
    if request.method == 'POST':
        form = TaskAddForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect(homepage)
    else:
        form = TaskAddForm()
    return render(request,'task_adding.html',{'form':form})
