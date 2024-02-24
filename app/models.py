from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Employee(models.Model):
    Emp_name=models.CharField(max_length=100)
    Emp_mobile_no=models.IntegerField()
    Employee_salary=models.BooleanField()
    def __str__(self):
        return self.Emp_name  
class project(models.Model):
    project_name=models.CharField(max_length=100)
    project_amoumt=models.BooleanField()
    project_details=models.TextField()
    def __str__(self):
        return self.project_name
class Task(models.Model):
    project= models.ForeignKey(project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.IntegerField(default=0)
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    def __str__(self):
        return self.title
class TaskDetail(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    task_name=models.CharField(max_length=100)
    task_no=models.IntegerField()
    task_details=models.TextField()
    def __str__(self):
        return self.task_name
class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.message}'
class AssignedTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.assigned_to.username}'s assignment of '{self.task.title}'"
