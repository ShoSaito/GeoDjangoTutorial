from rest_framework.serializers import ModelSerializer
from .models import WorldBorder

class WorldBorderSerializer(ModelSerializer):
    class Meta:
        model = WorldBorder
        fields = '__all__'