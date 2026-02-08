from django.contrib import admin
from django.urls import path
from .views import TodoListCreate, TodoRetrieveUpdateDelete
urlpatterns = [
    path('todos/', TodoListCreate.as_view()),
    path('todos/<int:pk>/', TodoRetrieveUpdateDelete.as_view()),
]
