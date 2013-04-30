from django.db import models

class User_ID(models.Model):
    
    user_ip = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user_ip

class User_Event(models.Model):
    
    user_id = models.ForeignKey(User_ID)
    enter_time = models.DateTimeField(null=True)
    page_link = models.CharField(max_length=200)
    time_on_page = models.IntegerField(null=True)


    def __unicode__(self):
        return self.page_link


class User_Project_Lock(models.Model):
    
    user_id = models.ForeignKey(User_ID)
    project_lock = models.DateTimeField(null=True)
    project_link = models.CharField(max_length=200)


    def __unicode__(self):
        return self.project_link
