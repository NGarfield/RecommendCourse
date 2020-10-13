from rest_framework import generics
from backend.models import Subject,Calender,Register,Group,SubjectCondition
from backend.api.serializers import (SubjectSerializers,CalenderSerializer,
                                     RegisterSerializer,GroupSerializer,
                                     SubjectConditionSerializer)

class SubjectListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Subject.objects.filter(name_group_id=2)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers


class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Subject.objects.filter(name_group_id=2)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers


class CalenderListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Subject.objects.filter(name_group_id=2)
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer

class RegisterListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Register.objects.filter(name_group_id=2)
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class GroupListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Register.objects.filter(name_group_id=2)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SubjectConditionListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Register.objects.filter(name_group_id=2)
    queryset = SubjectCondition.objects.all()
    serializer_class = SubjectConditionSerializer