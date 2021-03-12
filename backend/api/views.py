from rest_framework import generics,mixins
from backend.models import Subject,Calender,Register,Group,SubjectCondition
from backend.api.serializers import (SubjectSerializers,CalenderSerializer,
                                     RegisterSerializer,GroupSerializer,
                                     SubjectConditionSerializer)
import json
from django.http import HttpResponse

class SubjectListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Subject.objects.filter(name_group_id=2)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers


class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Subject.objects.filter(name_group_id=2)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers


class CalenderListCreateAPIView(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                generics.GenericAPIView):
    # queryset = Subject.objects.filter(name_group_id=2)
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        mydata = json.loads(request.body)
        print(mydata)
        self.create(request, *args, **kwargs)
        return HttpResponse("Got json data")

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