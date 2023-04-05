from django.contrib import admin
from .models import *

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ["subject","clas", "level", "question", "correct" ]
    list_filter = ["subject", "clas"]
    list_editable = ["clas", "level"]

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ["clas", "subject", "level", "is_active", "deadline"]
    list_filter = ["subject", "clas"]

admin.site.register(Subject)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "result", "created_at"]