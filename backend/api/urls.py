from django.urls import path
from backend.api.views import ( SubjectListCreateAPIView,
                                SubjectDetailAPIView,
                                CalenderListCreateAPIView,
                                RegisterListCreateAPIView,
                                GroupListCreateAPIView,
                                SubjectConditionListCreateAPIView)

urlpatterns = [
    path("subjects/",SubjectListCreateAPIView.as_view(), name="subject-list"),
    path("calenders/",CalenderListCreateAPIView.as_view(), name="calender-list"),
    path("registers/",RegisterListCreateAPIView.as_view(), name="register-list"),
    path("groups/",GroupListCreateAPIView.as_view(), name="group-list"),
    path("subjectconditions/",SubjectConditionListCreateAPIView.as_view(), name="subjectCondition-list"),
    path("subjects/<int:pk>",SubjectDetailAPIView.as_view(), name="subject-detail"),
]
