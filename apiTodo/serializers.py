from rest_framework import fields, serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            "pk",
            'task',
            'done',
        ]