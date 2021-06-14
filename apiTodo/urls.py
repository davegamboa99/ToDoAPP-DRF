from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [

    
    path('todolist/', views.todoList, name="todoList"),
    path('todoCreate/', views.todoListCreate, name="todoCreate"),
    path('todoUpdate/<str:pk>/', views.todoListUpdate, name='todoUpdate'),
    path('todoDelete/<str:pk>/', views.todoDelete, name='todoDelete'),



]