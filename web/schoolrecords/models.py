from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=50, unique=True)
    grade = models.CharField(max_length=10)
    date_enrolled = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

