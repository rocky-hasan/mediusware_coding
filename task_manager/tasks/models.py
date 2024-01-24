from django.db import models
# Create your models here.


Priority_Choices=(
    ('low','low'),
    ('medium','medium'),
    ('high','high'),
)

class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='Task/',blank=True,null=True)
    create_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField()
    priority=models.CharField(max_length=10,choices=Priority_Choices)
    is_complete=models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.title)
