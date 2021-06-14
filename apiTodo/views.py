from .models import Todo
from .serializers import TodoSerializer

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.





@api_view(['GET'])
def todoList(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)