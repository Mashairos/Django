from django.urls import path
from . import views 

urlpatterns = [
    path('', views.taskList, name="taskList"),
    path('task/<int:id>', views.taskView, name="taskView"),
    path('newtask/', views.taskNew, name="taskNew"),
    path('edit/<int:id>', views.taskEdit, name="taskEdit"),
    path('delete/<int:id>', views.taskDelete, name="taskDelete"),
    path('change/<int:id>', views.taskChange, name="taskChange")
]