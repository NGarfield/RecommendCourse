from rest_framework import generics
from backend.models import Subject,Calender
from backend.api.serializers import SubjectSerializers,CalenderSerializer

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