from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveSmallIntegerField()
    school = models.ForeignKey(School,
        on_delete=models.CASCADE,
        related_name='students') # used in school detail to access all the students
        # so in views, the SchoolDetailView, which has as its model, a School, through it, you can access all the students
        # by saying "students", the related_name

    def __str__(self):
        return self.name