from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout
from django.contrib import messages
from . models import todo_mod
from django.contrib.auth.decorators import login_required

# Create your views here.cd /d D:\DJANGO\venv\Scripts
@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo_mod = todo_mod(user=request.user, todo_name=task)
        new_todo_mod.save()

    all_todo = todo_mod.objects.all()
    context = {
        'todo_list':all_todo
    }
    return render(request, 'todoapp/todo.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # password check
        if len(password)<8:
            messages.error(request,"Password must be atleast 8 charecters")
            return redirect('register')

        # user check
        get_users = User.objects.filter(username=name)
        if get_users:
            messages.error(request,"User already exist !")
            return redirect('register')


        new_user = User.objects.create_user(username=name, email=email, password=password)
        new_user.save()
        messages.success(request, "Registration suceessful! Log in now ")
        # return render(request, 'todoapp/login.html', {})
        return redirect('login')

    return render(request, 'todoapp/register.html', {})

def logout_view(request):
    logout(request)
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        check_user = authenticate(username=username, password = password)
        if check_user is not None:
            auth_login(request, check_user)
            return redirect('home-page')
        else:
            messages.error(request, "User does not exist")
            return redirect('login')
    
    return render(request, 'todoapp/login.html',{})

@login_required
def deleteTask(request,name):
    get_todo = todo_mod.objects.get(user=request.user, todo_name=name)
    get_todo.delete()
    return redirect('home-page')

@login_required
def completeTask(request, name):
    get_todo = todo_mod.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('home-page')

