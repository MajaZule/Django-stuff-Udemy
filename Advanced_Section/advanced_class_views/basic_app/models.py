from django.db import models


class School(models.Model):
    name = models.CharField(max_length = 300)
    principal = models.CharField(max_length = 300)
    location = models.CharField(max_length = 300)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length = 300)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
