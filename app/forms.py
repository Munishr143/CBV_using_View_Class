from app.models import *
from django import forms
class Student_Form(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'