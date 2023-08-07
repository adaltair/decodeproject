from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task_detail(request, id):
    task = get_object_or_404(Task, id=id, owner=request.user)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['owner'] = request.user
        serializer.validated_data['completed'] = False
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, owner=request.user)
    serializer = TaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, owner=request.user)
    task.delete()
    return Response(status=204)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def execute_task(request, id):
    task = get_object_or_404(Task, id=id, owner=request.user)
    task.completed = True
    task.save()
    return Response({"message": "Task marked as completed"})
