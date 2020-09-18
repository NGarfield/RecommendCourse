from django.urls import path
from backend.api.views import SubjectListCreateAPIView,SubjectDetailAPIView

urlpatterns = [
    path("subjects/",SubjectListCreateAPIView.as_view(), name="subject-list"),
    path("subjects/<int:pk>",SubjectDetailAPIView.as_view(), name="subject-detail"),
]
