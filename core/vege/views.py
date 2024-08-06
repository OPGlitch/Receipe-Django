import os

from django.shortcuts import render, redirect
from .models import *
# Create your views here.

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

def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    if(len(queryset.image)>0):
        os.remove(queryset.image.path)
    queryset.delete()
    return redirect('/receipes/')

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