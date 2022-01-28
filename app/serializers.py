from rest_framework import serializers
from .models import UserFile


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = '__all__'
