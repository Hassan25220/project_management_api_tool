from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .models import User, Project, ProjectMember, Task, Comment
from .serializers import UserSerializer, RegisterSerializer, ProjectSerializer, ProjectMemberSerializer, TaskSerializer, CommnetSerializer



# Create your views here.


# Register New user

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



# Project CRUD using Viewset
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


# Task APIs (Task are nested under Project)
# class TaskViewSet(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated]


#     def get_queryset(self):
#         project_id = self.kwargs['project_id']
#         return Task.objects.filter(project_id= project_id)
    
#     def perform_create(self, serializer):
#         project_id = self.kwargs['project_id']
#         project = Project.objects.get(id=project_id)
#         serializer.save(project=project)



class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Task.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        project = Project.objects.get(id=project_id)
        serializer.save(project=project)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]






class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommnetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_querset(self):
        task_id = self.kwargs['task_id']
        return Comment.objects.filter(task_id=task_id)

    def perform_create(self, seializer):
        task_id = self.kwargs['task_id']
        task = Task.objects.get(id=task_id)
        seializer.save(task=task, user=self.request.user)