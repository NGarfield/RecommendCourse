# Generated by Django 3.1.1 on 2020-10-08 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities_name', models.CharField(max_length=100)),
                ('activities_Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('year', models.IntegerField()),
                ('term', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=100)),
                ('facuty', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('all_credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_group', models.CharField(max_length=60)),
                ('number_of_credits', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.course')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_subject', models.CharField(max_length=10)),
                ('subjectName', models.CharField(max_length=70)),
                ('belongTo', models.CharField(max_length=50)),
                ('credit', models.IntegerField()),
                ('name_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.group')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.ManyToManyField(related_name='condition', to='backend.Subject')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=80)),
                ('major', models.CharField(max_length=80)),
                ('degree', models.IntegerField()),
                ('gpa', models.FloatField()),
                ('AnnountCreditEarned', models.IntegerField()),
                ('id_student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('term', models.IntegerField()),
                ('grade', models.FloatField(default=0.0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.subject')),
            ],
        ),
        migrations.CreateModel(
            name='joinActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_hour', models.TimeField()),
                ('activtities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.activities')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.student')),
            ],
        ),
    ]
