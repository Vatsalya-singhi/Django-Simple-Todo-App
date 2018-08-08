from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todo
# Create your views here.

def index(request):
    todos = todo.objects.all()
    content={
        'todow' : todos,
    }
    return render(request,'index.html',content)

def details(request,id):
    todoi = todo.objects.get(id=id)
    content={
        'todo' : todoi
    }
    return render(request,'details.html',content)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo1=todo(title=title,text=text)
        todo1.save()
        return redirect('/todos')
    else:
        return render(request,'add.html')

def delitem(request,id):
    todoi = todo.objects.get(id=id)
    todoi.delete()
    todo.objects.filter(id=id).delete()
    return redirect('/todos')
