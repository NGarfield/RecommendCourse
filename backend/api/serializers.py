from rest_framework import serializers
from backend.models import Subject,Calender

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = "__all__"