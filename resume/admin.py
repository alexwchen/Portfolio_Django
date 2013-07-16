from resume.models import Education, Job, Affiliation, Contact, Supervisor, Supervisor_Affiliation, Supervisor_Department, Supervisor_Famous_paper
from django.contrib import admin

###############################
#   Resume related models
###############################

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

###############################
#   Supervisor related models
###############################
class Supervisor_AffiliationInline(admin.TabularInline):
    model=Supervisor_Affiliation
    extra=0

class Supervisor_DepartmentInline(admin.TabularInline):
    model=Supervisor_Department
    extra=0

class Supervisor_Famous_paperInline(admin.TabularInline):
    model=Supervisor_Famous_paper
    extra=0

class SupervisorAdmin(admin.ModelAdmin):
    fieldsets=[
    ('Personal Info', {'fields':['name', 'email', 'position', 'university']}),
    ('Meta Info', {'fields':['contact', 'start_date', 'end_date', 'image_path', 'link']}),
    ('Tag Info', {'fields':['field', 'famous_paper', 'research_interest']}),
    ]

    inlines = [Supervisor_AffiliationInline,Supervisor_DepartmentInline,Supervisor_Famous_paperInline]

###############################
#   Contact related models
###############################

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
    inlines = [SupervisorInline]


###############################################
# the following section is not displayed due 
# to clearity of the admin interface
###############################################

#admin.site.register(Education, EducationAdmin)
admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(Supervisor,SupervisorAdmin)
admin.site.register(Job, JobsAdmin)
admin.site.register(Contact, ContactAdmin)
