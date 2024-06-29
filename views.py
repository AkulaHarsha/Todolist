from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .form import *
from .models  import *

# Create your views here.
@login_required(login_url='login')
#for the home page logic
def first(request):
     if request.user.is_authenticated:
        user=request.user
        form=TodoForm()
        todos=Todo.objects.filter(user=user).order_by('priority')
        return render(request,'index.html',context={'form':form,"todos":todos})
# for the login page
def Login(request):
    if request.method=="GET":
        form1=AuthenticationForm()
        context={
        "form":form1
                }
    
        return render(request,'login.html',context=context)
    elif request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user=authenticate(username = username,password=password)
           login(request,user)
           return redirect('home')
        else: 
            
            context={'form':form} 
            return render(request,'login.html',context=context)
# for the signup page            
def Signup(request):
    if request.method=="GET":
        form=UserCreationForm()
        context={
            "form":form
              }
        return render(request,'signup.html',context=context)
    elif request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #return HttpResponse("this form is valid")
            if user is not None:
                return redirect('login')    
              # Redirect to a success page
        else:    
            context={
                "form":form
            }
            return render(request,'signup.html',context=context)
# for the adding todo logic
@login_required(login_url='login')
def addtodo(request):
    if request.user.is_authenticated:
        user=request.user
        form=TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user=user
            todo.save()
            return redirect("home")
        else:
            return render(request,'index.html',context={'form':form})
# for the logic of logout todo    
def signout(request): 
    logout(request)
    return redirect('login')  
# for the todo deleting
def deletetodo(request,id): 
    Todo.objects.get(pk=id).delete()
    return redirect('home')

# for the chanaging todo status
def changetodo(request,id,status):
    update=Todo.objects.get(pk=id)
    update.status=status
    update.save()
    return redirect('home')