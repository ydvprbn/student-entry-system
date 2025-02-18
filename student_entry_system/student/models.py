from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.TextField()
    grade = models.CharField(max_length=10)
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.name
