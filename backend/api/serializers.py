from rest_framework import serializers
from backend.models import Subject,Calender,Register,Group,SubjectCondition

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class NameSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id_subject","subjectName")

class SubjectConditionSerializer(serializers.ModelSerializer):
    subject = NameSubjectSerializer(read_only=True)
    
    class Meta:
        model = SubjectCondition
        fields = "__all__"