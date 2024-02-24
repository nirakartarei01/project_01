from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Employee)
admin.site.register(project)
admin.site.register(Task)
admin.site.register(TaskDetail)
admin.site.register(ChatMessage)
admin.site.register(AssignedTask)
