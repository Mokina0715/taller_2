from django.db import models
from django.utils import timezone
from icfes.models import Category, Subject


class Subtopic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subtopics')
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['subject__name', 'name']

    def __str__(self):
        return f"{self.subject.name} - {self.name}"


class StudyMaterial(models.Model):
    RESOURCE_TYPES = [
        ('video', 'Video'),
        ('web', 'Página Web'),
        ('image', 'Imagen'),
        ('pdf', 'PDF'),
        ('note', 'Apunte'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    explanation = models.TextField()
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    link = models.URLField()
    seen = models.BooleanField(default=False)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name='materials')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['subtopic__subject__name', 'subtopic__name', 'title']

    def __str__(self):
        return self.title

    def get_type_display_icon(self):
        icons = {
            'video': '🎥',
            'web': '🌐',
            'image': '🖼️',
            'pdf': '📄',
            'note': '📝',
        }
        return icons.get(self.resource_type, '📚')
