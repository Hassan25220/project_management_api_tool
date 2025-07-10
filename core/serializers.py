from rest_framework import serializers
from .models import User, Project, ProjectMember, Task, Comment



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'date_joined']



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            'project': {'read_only': True}
        }

class CommnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'task': {'read_only': True},
            'user': {'read_only': True}
        }


        