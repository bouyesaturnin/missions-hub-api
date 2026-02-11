from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Tasks
from .serializers import TasksSerializer

# 1. LA CLASSE POUR LES TÂCHES (TasksViewSet)
class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # L'utilisateur ne voit que ses propres tâches
        return Tasks.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # On lie la tâche à l'utilisateur qui la crée
        serializer.save(owner=self.request.user)

# 2. LA FONCTION POUR L'INSCRIPTION (register_user)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Nom d\'utilisateur et mot de passe requis'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Cet utilisateur existe déjà'}, status=status.HTTP_400_BAD_REQUEST)

    User.objects.create_user(username=username, password=password)
    return Response({'message': 'Utilisateur créé avec succès'}, status=status.HTTP_201_CREATED)