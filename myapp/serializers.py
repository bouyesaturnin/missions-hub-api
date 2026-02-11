from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'completed', 'description', 'image']
        # On s'assure que title est bien requis mais on enlève les contraintes inutiles sur le reste
        extra_kwargs = {
            'title': {'allow_blank': False, 'required': True},
            'description': {'required': False, 'allow_null': True, 'allow_blank': True},
            'image': {'required': False, 'allow_null': True},
        }
        # Si owner est géré automatiquement par le ViewSet :
        read_only_fields = ('owner',)



