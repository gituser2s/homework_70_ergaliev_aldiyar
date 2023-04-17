from rest_framework import serializers
from webapp.models.tasks import StatusChoice, Task
from webapp.models.projects import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'start_date', 'end_date', 'is_deleted')
        read_only_fields = ('is_deleted',)


class TaskSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'description', 'detailed_description', 'type', 'status',
                  'created_at', 'updated_at', 'deleted_at', 'is_deleted', 'projects')
        read_only_fields = ('created_at', 'updated_at', 'deleted_at', 'is_deleted', 'projects')
