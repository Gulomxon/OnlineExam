from django.db import models
from django.contrib.auth.models import User, AbstractUser

class School(models.Model):
    # number = models.IntegerField()
    number = models.CharField(max_length=150, verbose_name="Maktab raqami")

    def __str__(self):
        return str(self.number)

class ClassChoices(models.IntegerChoices):
    FIRST = 0, '1-sinf'
    SECOND = 1, '2-sinf'
    THIRD = 2, '3-sinf'
    FOURTH = 3, '4-sinf'
    FIFTH = 4, '5-sinf'
    SIXTH = 5, '6-sinf'
    SEVENTH = 6, '7-sinf'
    EIGHT = 7, '8-sinf'
    NINE = 8, '9-sinf'
    TEN = 9, '10-sinf'
    ELEVEN = 10, '11-sinf'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(verbose_name="Sharif", max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    clas = models.IntegerField(choices=ClassChoices.choices, verbose_name="class")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)
