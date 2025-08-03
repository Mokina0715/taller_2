from django.contrib import admin
from .models import Category, Subject, Question, Exam, Answer, Certificado


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text', 'subject', 'correct_answer')
    list_filter = ('subject', 'subject__category')
    search_fields = ('text',)

    def short_text(self, obj):
        return obj.text[:50] + ('...' if len(obj.text) > 50 else '')
    short_text.short_description = 'Question Text'


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'date', 'score')
    list_filter = ('date',)
    search_fields = ('student_name',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam', 'question', 'selected_answer', 'is_correct')
    list_filter = ('is_correct', 'selected_answer')
    search_fields = ('question__text', 'exam__student_name')

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'exam')
    search_fields = ('exam__student_name',)
