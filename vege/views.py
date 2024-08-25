import os

from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'Username already exists.')
            return redirect("/register/")

        user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username
        )

        #used below to encrypt password, if added in object create directly then password won't be encrypted
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully.')

    context = {'page': 'register page'}
    return render(request, "register.html", context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.info(request, 'Invalid username.')
            return redirect("/login/")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, 'Invalid Password.')
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/receipes/")

    context = {'page': 'login page'}
    return render(request, "login.html", context)


def logout_page(request):
    logout(request)
    return redirect('/login')

@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        n = data.get("name")
        d = data.get("description")
        i = request.FILES.get('image')

        Receipe.objects.create(
            name = n,
            description = d,
            image = i )

        return redirect('/receipes/')

    query_set = Receipe.objects.all()

    if request.GET.get('search'):
        print(request.GET.get('search'))
        query_set = query_set.filter(name__icontains = request.GET.get('search'))

    context = {'page': 'Receipes page', 'receipes': query_set}
    return render(request, 'receipes.html', context)

@login_required(login_url="/login/")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    if(len(queryset.image)>0):
        os.remove(queryset.image.path)
    queryset.delete()
    return redirect('/receipes/')

@login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method=="POST":
        data = request.POST
        n = data.get("name")
        d = data.get("description")
        i = request.FILES.get('image')

        queryset.name = n
        queryset.description = d
        if i :
            if (len(queryset.image) > 0):
                os.remove(queryset.image.path)
            queryset.image = i

        queryset.save()
        return redirect('/receipes/')

    context = {'page': 'Update page', 'receipe_obj': queryset}
    return render(request, 'update_receipes.html', context)