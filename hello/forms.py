
from django import forms
from .models import Student, Blog 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name","age"]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content']        