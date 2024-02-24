from django.urls import path
from .views import *
from api.views import *
urlpatterns = [
  path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
  path('tasks/',projectlist.as_view(), name='project-list'),
    
   

    
]


 