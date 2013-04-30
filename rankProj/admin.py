from rankProj.models import Project, Feature, Project_Type
from django.contrib import admin

class FeatureInline(admin.StackedInline):
    model = Feature
    extra = 0
 
class ProjectTypeInline(admin.StackedInline):
    model = Project_Type
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
       ('Title', {'fields':['title', 'complete_date', 'authors']}),
       ('Project Rank', {'fields':['short_description', 'rank_img','link', 'tags', 'vote_up','base_vote']}),
       ('Content', {'fields':['motivation_content', 'motivation_image', 'video_url', 'PDF']}),
    ]
    list_display = ['title', 'base_vote', 'vote_up']
    inlines = [ProjectTypeInline, FeatureInline]

admin.site.register(Project, ProjectAdmin)
###############################################
# the following section is not displayed due 
# to clearity of the admin interface
###############################################

#admin.site.register(Feature)
#admin.site.register(Project_Type)
