from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from .models import Task
# Create your views here.
class TaskCreate(CreateView):
    model=Task
    fields='__all__'
    template_name='createtask.html'
    success_url=reverse_lazy('list-task')
    def get_queryset(self):
        return Task.objects.all()
    


class TaskList(ListView):
    model=Task
    template_name='home.html'
    context_object_name='all_data'

class TaskDetail(DetailView):
    model=Task
    template_name='taskdetail.html'
    context_object_name='data'
class TaskUpdate(UpdateView):
    model=Task
    fields='__all__'
    template_name='updatetask.html'
    success_url=reverse_lazy('list-task')
class TaskDelete(DeleteView):
    model=Task
    template_name='Deletetask.html'
    success_url=reverse_lazy('list-task')
