from django.urls import path
from .views import TaskCreate,TaskDetail,TaskList,TaskUpdate,TaskDelete

urlpatterns = [
    path('createtask/', TaskCreate.as_view(),name='create-task'),
    path('', TaskList.as_view(),name='list-task'),
    path('detailtask/<int:pk>/', TaskDetail.as_view(),name='detail-task'),
    path('updatetask/<int:pk>/', TaskUpdate.as_view(),name='update-task'),
    path('deletetask/<int:pk>/', TaskDelete.as_view(),name='delete-task'),


]
