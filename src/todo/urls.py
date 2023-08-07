from django.urls import path
from .views import (
    get_task_list,
    get_task_detail,
    create_task,
    edit_task,
    delete_task,
    execute_task,
    
)
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'tasks', Tez)

urlpatterns = [
    path('api/todo/', get_task_list),
    path('api/todo/<int:id>/', get_task_detail, name='task-detail'),
    path('api/todo/create', create_task, name='create-task'),
    path('api/todo/<int:id>/', edit_task, name='edit-task'),
    path('api/todo/<int:id>/', delete_task, name='delete-task'),
    path('api/todo/<int:id>/execute/', execute_task, name='execute-task'),
]
