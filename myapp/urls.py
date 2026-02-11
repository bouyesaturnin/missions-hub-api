from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet
from .views import register_user

router = DefaultRouter()
# On enregistre 'tasks' sans slash au début
router.register(r'tasks', TasksViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)), # Ceci inclut toutes les routes du routeur
    path('register/', register_user, name='register'),
]