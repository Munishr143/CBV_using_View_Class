from django.db import models

# Create your models here.
class Student(models.Model):
    Sid=models.IntegerField(primary_key=True)
    Sname=models.CharField(max_length=30)
    Sage=models.IntegerField()

    def __str__(self) -> str:
        return self.Sname
