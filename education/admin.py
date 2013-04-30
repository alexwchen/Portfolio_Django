from education.models import Material, Material_Type
from django.contrib import admin

class Material_TypeInline(admin.StackedInline):
    model = Material_Type
    extra = 0

class MaterialAdmin(admin.ModelAdmin):
    fields = ['title', 'date', 'description','image_url', 'source_url']
    list_display = ['title', 'date']
    inlines = [Material_TypeInline]


admin.site.register(Material, MaterialAdmin)
###############################################
# the following section is not displayed due 
# to clearity of the admin interface
###############################################

# admin.site.register(Material_Type)
