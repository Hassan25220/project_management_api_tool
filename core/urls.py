from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, RegisterUserView, UserDetailView, TaskListCreateView, TaskDetailView, CommentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



# Create router and register ProjectViewSet
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')



# Define URL patterns

urlpatterns = [
    # User endpoints
    path('users/register/', RegisterUserView.as_view()),
    path('users/login/', TokenObtainPairView.as_view()),   # login returns view
    path('users/<int:pk>/', UserDetailView.as_view()),

    # Project CRUD via router
    path('', include(router.urls)),

    # Tasks (nested in projects)
    # path('projects/<int:project_id>/tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('projects/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),

    path('projects/<int:project_id>/tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),


    # Comments (nested in tasks)
    path('tasks/<int:task_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))

]


from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Project Management API Tool",
        default_version="v1",
        description= "API docs for project management tool",
    ),
    public=True
)


urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]