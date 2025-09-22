from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name = "blogs")
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name
    


