from django.shortcuts import render,redirect
import time 
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse
from  django.contrib.auth.models import User
from django.contrib import messages
from  django.contrib.auth import authenticate,login
@csrf_exempt 
def recipe(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_desc=data.get('recipe_desc')
        recipe_img=request.FILES.get("recipe_img")
        
        Recipe.objects.create(
            recipe_name= recipe_name,
            recipe_desc=recipe_desc,
            recipe_img=recipe_img
            )
        return redirect("")
    
    
    

    return render(request,"recipe.html")


def show(request):
    queryset=Recipe.objects.all()
    find=request.GET.get('search')
    if find:  
       queryset=queryset.filter(recipe_name__icontains= find)
       
    return render(request,"show.html",context={"queryset":queryset})

def signup(request):
    if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")

            user=User.objects.filter(username=username)
            if user.exists():
                messages.warning(request, "account with this username already exist")
                return redirect('/signup/')
        
            user=User.objects.create(
            username=username,
            password=password
            )
            user.set_password(password)
            user.save()
            # messages.info(request, "account is created ")
            return redirect("login/")




    return render(request,"signup.html")



def Login_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not (User.objects.filter(username=username).exists()):
            messages.error(request,"invalid credentials")
            return redirect("login/")

        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"inavalid credentials")
            return redirect('/login/')
        
        login(request,user)
        return redirect("/")


    return render(request,"login.html")

   
       

    



def delete(request,id):
    set=Recipe.objects.get(id=id)
    set.delete()
    return redirect("/show/")


def update(request,id):
    set=Recipe.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_desc=data.get('recipe_desc')
        recipe_img=request.FILES.get("recipe_img")

       
        set.recipe_name=recipe_name
        set.recipe_desc=recipe_desc
        if recipe_img:
          set.recipe_img=recipe_img


        set.save()
        return redirect('/show/')
       
       
       
        






    context={"set":set}
    return render(request,"update.html",context)