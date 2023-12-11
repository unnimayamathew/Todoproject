
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from . models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView, DeleteView



class tasklistview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='task'

class taskdetailview(DetailView):
    model=Task
    template_name='details.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name = 'task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# create your views here.
def home(request):
    task1=Task.objects.all()
    if request.method=='post':
        name=request.post.get('task','')
        priority=request.post.get('priority','')
        date=request.post.get('date','')

        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"home.html",{'task':task1})

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=='post':
        task.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoform(request.post or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{'f':f,'task':task})
