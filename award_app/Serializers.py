from rest_framework import serializers
from .models import Image,Profile
class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('title', 'description', 'comments')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'name')
