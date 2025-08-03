from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam, Question, Answer, Certificado, Subject, Category
import random

def index(request):
    subjects = Subject.objects.all()
    categories = Category.objects.all()
    exams = Exam.objects.all().order_by('-date')
    context = {
        'exams': exams, 
        'categories': categories,
        'subjects': subjects
    }
    return render(request, 'index.html', context)

def exam_start(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        category = request.POST.get('category')
        subject = request.POST.get('subject')
        print(f"Selected category: {category}")
        query = Question.objects
        if category and category.isdigit():
            query = query.filter(subject__category__id=category)
        if subject and subject.isdigit():
            query = query.filter(subject__id=subject)
        
        all_questions = list(query.all())
        selected_questions = random.sample(all_questions, min(10, len(all_questions)))

        exam = Exam.objects.create(student_name=student_name)
        exam.questions.set(selected_questions)
        exam.save()

        request.session['exam_id'] = exam.id
        request.session['question_index'] = 0

        return redirect('exam_question')

    category = request.GET.get('category')
    subject = request.GET.get('subject')
    return render(request, 'exam_start.html', {'category': category, 'subject': subject})


def exam_question(request):
    exam_id = request.session.get('exam_id')
    index = request.session.get('question_index', 0)

    exam = get_object_or_404(Exam, id=exam_id)
    questions = list(exam.questions.all())

    if index >= len(questions):
        return redirect('exam_result')

    question = questions[index]

    if request.method == 'POST':
        selected = request.POST.get('respuesta')
        is_correct = question.correct_answer == selected

        Answer.objects.create(
            exam=exam,
            question=question,
            selected_answer=selected,
            is_correct=is_correct
        )

        request.session['question_index'] = index + 1

        if index + 1 >= len(questions):
            total_correct = Answer.objects.filter(exam=exam, is_correct=True).count()
            exam.score = round((total_correct / len(questions)) * 100, 2)
            exam.save()
            return redirect('exam_result')
        else:
            return redirect('exam_question')

    return render(request, 'exam_question.html', {'pregunta': question})


def exam_result(request):
    exam_id = request.session.get('exam_id')
    exam = get_object_or_404(Exam, id=exam_id)

    return render(request, 'exam_result.html', {'exam': exam})

def view_certificado(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if exam.score == 100.00:
        certificado = Certificado.objects.filter(exam=exam).first()
        if not certificado:
            certificado = Certificado.objects.create(exam=exam) 
    return render(request, 'certificado.html', {'certificado': certificado})