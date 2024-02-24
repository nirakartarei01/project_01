from rest_framework import serializers
from rest_framework import serializers
from app.models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = project,Task,TaskDetail,ChatMessage,AssignedTask
        fields = '__all__'