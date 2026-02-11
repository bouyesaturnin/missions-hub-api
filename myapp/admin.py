from django.contrib import admin

from myapp.models import Tasks

# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_created', 'completed')
    list_filter = ('completed', 'date_created')
    search_fields = ('title', 'description')

admin.site.register(Tasks, TasksAdmin)