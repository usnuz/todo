from django.shortcuts import render, redirect
from .models import *

def index_view(request):
    if request.method == "POST":
        item = request.POST.get("item")
        Todo.objects.create(item=item)

        return redirect('index')
    context = {
        'data': Todo.objects.all()
    }
    return render(request, 'index.html', context)
    
    
def delete(request, pk):
    a = Todo.objects.get(id=pk)
    a.status = 2
    a.save()
    return redirect('index')

def finish(request, pk):
    a = Todo.objects.get(id=pk)
    a.status = 3
    a.save()
    return redirect('index')
    
    
def inprog(request):
    if request.method == "POST":
        search = request.POST.get('search')
        ss = Todo.objects.filter(item__icontains=search)
        return render(request, 'inprog.html', {'data': ss})
    a = Todo.objects.filter(status=1)
    context = {"data": a}
    return render(request, 'inprog.html', context)
    
   
def deleted(request):
    if request.method == "POST":
        search = request.POST.get('search')
        ss = Todo.objects.filter(item__icontains=search)
        return render(request, 'deleted.html', {'data': ss})
    a = Todo.objects.filter(status=2)
    context = {"data": a}
    return render(request, 'deleted.html', context)
    
    
def finished(request):
    if request.method == "POST":
        search = request.POST.get('search')
        ss = Todo.objects.filter(item__icontains=search)
        return render(request, 'finished.html', {'data': ss})
    a = Todo.objects.filter(status=3)
    context = {"data": a}
    return render(request, 'finished.html', context)


def search(request):
    if request.method == "POST":
        search = request.POST.get('search')
        ss = Todo.objects.filter(item__icontains=search)
        return render(request, 'index.html', {'data': ss})
    context = {
        'data': Todo.objects.all()
    }
    return render(request, 'index.html', context)