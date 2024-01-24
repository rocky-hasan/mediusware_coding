from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=['title','description','create_date','due_date']
admin.site.register(Task,TaskAdmin)
