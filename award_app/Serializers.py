from rest_framework import serializers
from .models import Image
class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('title', 'description', 'comments')
