from user_vote.models import User_ID, User_Event, User_Project_Lock
from django.contrib import admin

class User_Project_LockInline(admin.TabularInline):
    model = User_Project_Lock
    extra = 0

class User_EventInline(admin.TabularInline):
    model = User_Event
    extra = 0

class User_IDAdmin(admin.ModelAdmin):

    fields = ['user_ip']  
    inlines = [User_EventInline, User_Project_LockInline]

admin.site.register(User_ID, User_IDAdmin)
admin.site.register(User_Event)
admin.site.register(User_Project_Lock)
