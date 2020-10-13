from django.contrib import admin
from backend.models import (Activities,Student,joinActivity,Course,
                             Subject,Register,Group,Calender,SubjectCondition)


admin.site.register(Activities)
admin.site.register(Student)
admin.site.register(joinActivity)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Register)
admin.site.register(Group)
admin.site.register(Calender)
admin.site.register(SubjectCondition)