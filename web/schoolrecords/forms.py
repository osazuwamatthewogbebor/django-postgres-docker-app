# /workspaces/django-postgres-docker-app/web/schoolrecords/forms.py

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'grade']