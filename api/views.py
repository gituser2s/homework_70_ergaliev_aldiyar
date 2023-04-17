from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import TaskSerializer, ProjectSerializer
from webapp.models.tasks import Task
from webapp.models.projects import Project


class TasksView(APIView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all().exclude(is_deleted=True)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskDetailView(APIView):
    def get(self, *args, **kwargs):
        task = Task.objects.all().exclude(is_deleted=True)
        serializer = TaskSerializer(task[kwargs['pk']-1], many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskUpdateView(APIView):
    def put(self, request, pk, *args, **kwargs):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDeleteView(APIView):
    def delete(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(f"Удалено задание: {task.id}", status=status.HTTP_204_NO_CONTENT)

class ProjectsView(APIView):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all().exclude(is_deleted=True)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectDetailView(APIView):
    def get(self, *args, **kwargs):
        project = Project.objects.all().exclude(is_deleted=True)
        serializer = ProjectSerializer(project[kwargs['pk']-1], many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectUpdateView(APIView):
    def put(self, request, pk, *args, **kwargs):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDeleteView(APIView):
    def delete(self, request, pk):
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response(f"Удалён проект: {project.id}", status=status.HTTP_204_NO_CONTENT)
