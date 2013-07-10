from resume.models import Education, Job, Affiliation, Images, Contact, Supervisor
from django.contrib import admin

class JobsAdmin(admin.ModelAdmin):
    fields = [
    'title',
    'job_type',
    'company',
    'period',
    'start_date',
    'end_date',
    'detail'
    ]

class EducationAdmin(admin.ModelAdmin):
    fields = [
    'title',
    'degree',
    'program',
    'duration',
    'skills_programming_languages',
    'skills_design_tools',
    ]

class AffiliationAdmin(admin.ModelAdmin):
    fields= [
    'title',
    'period',
    ]

class ImageInline(admin.StackedInline):
    model=Images
    extra=0

class SupervisorInline(admin.StackedInline):
    model=Supervisor
    extra=0

class ContactAdmin(admin.ModelAdmin):
    fields= [
    'title_contact',
    'email',
    'title_research',
    'research_interest',
    ]
    inlines = [ImageInline, SupervisorInline]

admin.site.register(Job, JobsAdmin)
###############################################
# the following section is not displayed due 
# to clearity of the admin interface
###############################################

#admin.site.register(Education, EducationAdmin)
#admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(Contact, ContactAdmin)
