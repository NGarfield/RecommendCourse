from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    id_student = models.OneToOneField(User, on_delete=models.CASCADE)
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=80)
    major = models.CharField(max_length=80)
    degree = models.IntegerField()
    gpa = models.FloatField()
    AnnountCreditEarned = models.IntegerField()

    def __str__(self):
        return f"{ self.id_student } { self.frist_name } {self.last_name}"
    
class Activities(models.Model):
    activities_name = models.CharField(max_length=100)
    activities_Type = models.CharField(max_length=100)
    def __str__(self):
        return self.activities_name

class joinActivity(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    activtities = models.ForeignKey(Activities,on_delete=models.CASCADE)
    activity_hour = models.TimeField()
    def __str__(self):
        return f"{ self.student } { self.activtities }"


class Course(models.Model):
    course_id = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    facuty = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    year = models.IntegerField()
    all_credit = models.IntegerField()
    def __str__(self):
        return f"{self.course_id} {self.course_name}"

class Group(models.Model):
    name_group = models.CharField(max_length=60)
    number_of_credits = models.IntegerField()
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name_group
    

class Subject(models.Model):
    id_subject = models.CharField(max_length=10)
    subjectName = models.CharField(max_length=50)
    belongTo = models.CharField(max_length = 50)
    credit = models.IntegerField()
    coureseCondition = models.TextField()
    name_group = models.ForeignKey(Group,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id_subject} {self.subjectName}"

class Register(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    year = models.IntegerField()
    term = models.IntegerField()
    grade = models.FloatField()
    def __str__(self):
        return f"{self.subject} {self.student}"

class Calender(models.Model):
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField() 
    year = models.IntegerField()
    term = models.IntegerField()
    def __str__(self):
        return self.description
