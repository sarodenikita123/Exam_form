from django.db import models


class Exam(models.Model):
    gen = [("WOMEN", "women"), ("MEN", "men"), ("OTHER", "other"), ("GIRL", "girl"), ("BOY", "boy")]
    student_name = models.CharField(max_length=20)
    register_number = models.IntegerField()
    register_course = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=gen, default=True)
    exam_start = models.DateField()
    exam_end = models.DateField()
    comments = models.CharField(max_length=20)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)


