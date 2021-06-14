from .models import Todo
from .serializers import TodoSerializer

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.





@api_view(['GET'])
def todoList(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def todoListCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)   

@api_view(['POST', 'GET'])
def todoListUpdate(request, pk):
    queryset = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance = queryset, data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
    queryset = Todo.objects.get(id=pk)
    queryset.delete()

    return Response(serializer.data,"Item deleted")

