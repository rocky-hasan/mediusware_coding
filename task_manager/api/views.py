from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from .serializers import TaskSerialize
from tasks.models import Task


class TaskCreate_api(generics.ListCreateAPIView):
    data=Task.objects.all()
    serializer_class=TaskSerialize
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class TaskDetail_Api(generics.RetrieveUpdateDestroyAPIView):
    data=Task.objects.all()
    serializer_class=TaskSerialize

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    # put using for update
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    # delete data
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

