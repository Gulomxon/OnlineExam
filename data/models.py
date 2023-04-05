import threading
from datetime import datetime, timedelta
from django.utils import timezone
from django.db import models
from account.models import Student
# from onlinexem.account.models import Student
from django.db.models.signals import post_save
from django.dispatch import receiver


class Subject(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Test(models.Model):
    CHOICES = (
        (0, "1-sinf"),
        (1, "2-sinf"),
        (2, "3-sinf"),
        (3, "4-sinf"),
        (4, "5-sinf"),
        (5, "6-sinf"),
        (6, "7-sinf"),
        (7, "8-sinf"),
        (8, "9-sinf"),
        (9, "10-sinf"),
        (10, "11-sinf"),
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    clas = models.IntegerField(choices=CHOICES, verbose_name="sinf", default=0)
    question = models.TextField()
    correct = models.TextField()
    incorrect1 = models.TextField()
    incorrect2 = models.TextField()
    incorrect3 = models.TextField()

    def __str__(self):
        return self.question

class Exam(models.Model):
    CHOICES = (
        (0, "1-sinf"),
        (1, "2-sinf"),
        (2, "3-sinf"),
        (3, "4-sinf"),
        (4, "5-sinf"),
        (5, "6-sinf"),
        (6, "7-sinf"),
        (7, "8-sinf"),
        (8, "9-sinf"),
        (9, "10-sinf"),
        (10, "11-sinf"),
    )
    clas = models.IntegerField(choices=CHOICES, verbose_name="sinf")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    deadline = models.DateTimeField(verbose_name="boshlanish vaqti")
    duration = models.TimeField(verbose_name="tugash vaqti")
    level = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

# @receiver(post_save, sender=Exam)
# def exam_receiver(sender, instance, created, **kwargs):
#     if created:
#         one_hour_from_now = instance.deadline + instance.duration
#         time_difference = (one_hour_from_now - timezone.now()).total_seconds()
#         if time_difference > 0:
#             timer = threading.Timer(time_difference, my_function, args=[instance])
#             timer.start()
#         else:
#             instance.is_active = False
#             instance.save()
     #######################
def exam_receiver(sender, instance, created, **kwargs):
    # one_hour_from_now = instance.deadline + instance.duration # calculate the time one hour from deadline
    one_hour_from_now = datetime.now() + timedelta(minutes=1)
    timer = threading.Timer((one_hour_from_now - datetime.now()).total_seconds(), my_function, args=[instance])
    timer = threading.Timer((one_hour_from_now - datetime.now()).total_seconds(), my_function, args=[instance])
    timer.start()


def my_function(exam):
    pass
    # exam.is_active=False
    # exam.save()
    

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    result = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.student.user.username

