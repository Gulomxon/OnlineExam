from django.shortcuts import render
import pandas as pd
from .models import *
import random
from account.models import Student

def upload_file(request):
    if request.method == 'POST':
        data = request.POST
        subject = data.get('subject')
        clas = data.get('clas')
        level = data.get('level')
        file = request.FILES.get('file')

        df = pd.read_excel(file,sheet_name='Test')
        fields = list(df.columns)
        sub = Subject.objects.get(title = subject)

        # Create model instances and save to the database
        for index, row in df.iterrows():
            my_model = Test(
                subject=sub,
                clas=clas,
                level = level,
                question=row['savol'],
                correct=row['javob'],
                incorrect1=row['xato1'],
                incorrect2=row['xato2'],
                incorrect3=row['xato3']
            )
            my_model.save()
        return render(request, 'upload.html')
    elif request.method=="GET":
        content = {}
        content['subjects'] = Subject.objects.all()
        clas = Test.CHOICES
        content['classes'] = clas

        return render(request, 'upload.html', content)


def get_test(request, id):
    if request.method == "GET":
        exam = Exam.objects.get(id= id)
        subject = exam.subject
        clas = exam.clas
        level = exam.level
        tests = Test.objects.filter(clas = clas, subject = subject, level = level)
        test = tests.order_by('?')[:25]
        obj = []
        for i in test:
            obj.append(random.sample([i.correct, i.incorrect1, i.incorrect2, i.incorrect3], 4))
        for i in range(len(test)):
            test[i].correct, test[i].incorrect1, test[i].incorrect2, test[i].incorrect3 = obj [i]

        content = {}
        content["tests"] =test
        return render(request, 'test.html', content)
    elif request.method == "POST":
        data= request.POST
        result = 0
        a= data.get("1")
        question = Test.objects.get(id = int(a))
        sub = question.subject
        subject = Subject.objects.get(title = sub)
        for i in range(1, 5):
            if data.get(str(i)):
                a = data.get(str(i))
                answer = data.get(a)
                verify = Test.objects.get(id=int(a))
                # print(answer, " ", verify.correct)
                if verify.correct == answer:
                    result += 1
                    # print(result)

        student_id = request.user.id
        student = Student.objects.get(id = student_id)
        final = Result(student = student, subject= subject, result = result)
        final.save()
        content = {}
        content['final'] = final
        return render(request, "result.html", content)


