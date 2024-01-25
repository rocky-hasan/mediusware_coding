from typing import Any
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
    
    # Here searching query work also show data
class TaskList(ListView):
    model=Task
    template_name='home.html'
    context_object_name='all_data'

    def get_queryset(self):
        query=self.request.GET.get('q')
        queryset=Task.objects.all()
        if query:
            queryset=queryset.filter(title__icontains=query)
        return queryset
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    


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
