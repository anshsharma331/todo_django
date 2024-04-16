from django.contrib import admin
from .models import Todo, SubTask

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_by', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title', 'description')

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('todo', 'title', 'completed')
    list_filter = ('completed',)
    search_fields = ('title',)