from django.contrib import admin
from app1.models import Job
from .models import Resume

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('job_title', 'company_location', 'salary', 'experience_level', 'employment_type')
    
    # Fields to filter data in the sidebar
    list_filter = ('experience_level', 'employment_type', 'work_setting', 'company_size')
    
    # Fields that are searchable
    search_fields = ('job_title', 'company_location', 'employee_residence')
    
admin.site.register(Job)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['user', 'uploaded_at']
