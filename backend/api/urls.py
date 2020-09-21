from django.urls import path
from backend.api.views import SubjectListCreateAPIView,SubjectDetailAPIView,CalenderListCreateAPIView

urlpatterns = [
    path("subjects/",SubjectListCreateAPIView.as_view(), name="subject-list"),
    path("calenders/",CalenderListCreateAPIView.as_view(), name="calender-list"),
    path("subjects/<int:pk>",SubjectDetailAPIView.as_view(), name="subject-detail"),
]
