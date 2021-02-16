from exam.controllers import ExamController
from question.controllers import AnswerController
from user.controllers import OrganizerController
from user.models import User
from question.models import Question
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Assignment, Exam
from .forms import QuestionForm
import datetime
from django.views.decorators.csrf import csrf_exempt

userid = 'USR2021020001'
usermail = 'engin123@hotmail.com'


@csrf_exempt
def exam_detail(request, exam_id):
    examView = ExamController(exam_id).exam_show()
    questions = examView.questions
    email = request.session['user']
    user = User.objects.filter(mail=email).get()
    if request.method == 'POST':
        i = len(request.POST.getlist('question_id'))
        print(request.POST)
        asgment = Assignment.objects.filter(user_id=user.id,
                                            exam_id=exam_id).get()
        for j in range(i):
            AnswerController.answer(
                request.POST.getlist('question_id')[j], asgment,
                request.POST.getlist('choice')[j])

        a = ExamController(exam_id).result_calculate(email)
        print(a)
    return render(request, 'solvee.html', {
        'questions': questions,
        'student': not user.is_organizer
    })


def exam_index(
    request
):  #student için farklı sayfayı instructor için farklı sayfayı render eder.
    isOrganizer = False  #a is organizer değişkeni olarak düşünün

    if isOrganizer:
        exams = Exam.objects.all()
        return render(request, 'instructor.html', {'exams': exams})

    else:
        return 0


@csrf_exempt
def exam_delete(request, exam_id):
    print(exam_id)
    deleted = Exam.objects.filter(id=exam_id).get()
    deleted.delete()
    return redirect('../../../../main/instructor')


def exam_scores(request, exam_id):
    ass = ExamController(exam_id).examscores()
    return render(request, 'scores.html', {'assignments': ass})


@csrf_exempt
def exam_create(request):
    users = User.objects.filter(is_organizer=0)
    if request.method == 'POST':
        questnum = len(request.POST.getlist('question'))
        uscon = OrganizerController(usermail)
        date = datetime.datetime(2021, 2, 16)
        start = datetime.time(12, 30)
        end = datetime.time(15, 30)
        start_dt = datetime.datetime.combine(date.date(), start)
        end_dt = datetime.datetime.combine(date.date(), end)
        quiz = uscon.create_exam(request.POST['exam_name'], start_dt, end_dt)
        for i in range(questnum):
            ExamController(quiz.id).question_add(
                request.POST.getlist('question')[i],
                request.POST.getlist('ans_1')[i],
                request.POST.getlist('ans_2')[i],
                request.POST.getlist('ans_3')[i],
                request.POST.getlist('ans_4')[i],
                request.POST.getlist('correct_answer')[i])
        for student in request.POST.getlist('students'):
            ExamController(quiz.id).assign(student)
        return redirect('../../main/instructor')
    return render(request, 'createExam.html', {'users': users})
