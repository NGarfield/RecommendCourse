from rest_framework import generics
from backend.models import Subject
from backend.api.serializers import SubjectSerializers

class SubjectListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Subject.objects.filter(name_group_id=2)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers


class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Subject.objects.filter(name_group_id=2)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers