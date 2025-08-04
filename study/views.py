from django.shortcuts import render, get_object_or_404, redirect
from .models import Subtopic, StudyMaterial, Subject
from icfes.models import Category

def subject_list(request):
    categories = Category.objects.all()
    return render(request, 'subject_list.html', {'categories': categories})

def subtopic_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subtopics = Subtopic.objects.filter(subject__category=category)
    return render(request, 'subtopic_list.html', {'category': category, 'subtopics': subtopics})

def material_list(request, subtopic_id):
    subtopic = get_object_or_404(Subtopic, id=subtopic_id)
    materials = subtopic.materials.all()
    return render(request, 'material_list.html', {'subtopic': subtopic, 'materials': materials})

def material_detail(request, material_id):
    material = get_object_or_404(StudyMaterial, id=material_id)

    if request.method == 'POST':
        material.seen = True
        material.save()
        return redirect('material_detail', material_id=material.id)

    return render(request, 'material_detail.html', {'material': material})
