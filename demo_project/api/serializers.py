from rest_framework import serializers
from demoApp.models import Project


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project 
        fields = '__all__'
    

