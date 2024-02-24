from django.urls import path
from .views import *
from app.views import *

urlpatterns = [
    
   
    path('', login, name='login'),
    path('', signup, name='signup'),
    path('', create_task, name='createtask'),
    
]