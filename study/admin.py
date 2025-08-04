from django.contrib import admin
from .models import Subtopic, StudyMaterial

@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    list_filter = ('subject',)
    search_fields = ('name', 'subject__name')

@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtopic', 'resource_type', 'seen', 'created_at')
    list_filter = ('resource_type', 'seen', 'subtopic__subject')
    search_fields = ('title', 'subtopic__name', 'subtopic__subject__name')
