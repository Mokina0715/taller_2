from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('category/<int:category_id>/', views.subtopic_list, name='subtopic_list'),
    path('subtopic/<int:subtopic_id>/', views.material_list, name='material_list'),
    path('material/<int:material_id>/', views.material_detail, name='material_detail'),
]
