from rest_framework import serializers
from backend.models import Subject

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"