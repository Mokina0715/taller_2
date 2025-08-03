from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', views.index, name='index'),
    path('examen/iniciar/', views.exam_start, name='exam_start'),
    path('examen/pregunta/', views.exam_question, name='exam_question'),
    path('examen/resultado/', views.exam_result, name='exam_result'),
    path('examen/certificado/<int:exam_id>/', views.view_certificado, name='view_certificado'),
]
