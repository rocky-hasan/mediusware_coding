from rest_framework import serializers
from tasks.models import Task

class TaskSerialize(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['title','task_type_names','description','create_date','due_date']