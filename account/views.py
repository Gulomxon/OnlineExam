from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from .models import Student
from data.models import *
from datetime import datetime


def login_view(request):
    if request.method== "POST":
        content = {}
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            content["error"] = "Error"
            return render(request, "login.html", content)
    return render(request, "login.html")




def home(request):
    student_id = request.user.id
    student = Student.objects.get(id = student_id)
    content = {}
    clas = student.clas
    exams = Exam.objects.filter(clas=clas, is_active=True)
    content["exams"] = exams
    return render(request, "home.html", content)

class RegisterView(TemplateView):
    template_name = "login/registration.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        data = request.POST
        lastname = data.get('lastname')
        firstname = data.get('firstname')
        middlename = data.get('middlename')
        school = data.get('school')
        clas = data.get('clas')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')
        password2 = data.get('password2')
        doc_ser = data.get('doc_ser')
        doc_num = data.get('doc_numb')
        if password!= password2:
            messages.error(request, "parollar birxil emas")
            return redirect(reverse("reg"))




